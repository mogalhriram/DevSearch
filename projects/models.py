from django.db import models
import uuid
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
    decription = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    sorce_link = models.CharField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null= True, blank=True, default='default.jpg')
    tag = models.ManyToManyField(Tag, blank= True)
    vote_total = models.IntegerField(default=0, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.title

    

class Review(models.Model):
    VOTE_TYPE =(
        ('up','upvote'),
        ('down', 'downvote')
    )

    #owner=
    project = models.ForeignKey(Project, on_delete= models.CASCADE) #delete if project is deleted
    body =  models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.value

