from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile



class TagSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProfileSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProjectSearilizer(serializers.ModelSerializer):
    owner = ProfileSearilizer(many=False)
    tag = TagSearilizer(many=True)
    reviews = serializers.SerializerMethodField() #Add field to JSON data
   
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_reviews(self, obj):  
        reviews = obj.review_set.all()
        serializers = ReviewSearilizer(reviews, many=True)
        return serializers.data





