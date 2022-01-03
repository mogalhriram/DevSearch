from django.db import models
import uuid

from users.models import Profile

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link =models.CharField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null= True, blank=True, default='default.jpg')
    tag = models.ManyToManyField(Tag, blank= True)
    vote_total = models.IntegerField(default=0, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]  #highest rated project will be shown first

    @property
    def reviewers(self):
        query_set = self.review_set.all().values_list('owner__id', flat = True)
        return query_set


    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value ='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes/totalVotes) * 100

        self.vote_ratio = ratio
        self.vote_total = totalVotes

        self.save()
    

class Review(models.Model):
    VOTE_TYPE =(
        ('up','upvote'),
        ('down', 'downvote')
    )

    owner= models.ForeignKey(Profile,  null= True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete= models.CASCADE) #delete if project is deleted
    body =  models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    
    class Meta:
        unique_together = [['owner','project']] #will ensure one review per project by owner

    
    def __str__(self) -> str:
        return (str(self.owner) +" "+ str(self.project)+" "+ str(self.value) )

