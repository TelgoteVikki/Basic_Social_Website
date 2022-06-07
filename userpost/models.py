from django.db import models



# Create your models here.
#model for user credential
class Users_login(models.Model):
    userName=models.CharField(max_length=50)
#Model for  post data 
class Post_vote(models.Model):
    postName=models.CharField(max_length=50)
#model for user  post voting 
class User_post(models.Model):
    postID=models.IntegerField()
    user_Id=models.IntegerField()
    upvote_User=models.IntegerField()
    downvote_User=models.IntegerField()