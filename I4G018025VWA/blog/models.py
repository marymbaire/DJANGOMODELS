from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    title_text= models.CharField(max_length=200)
    text= models.TextField()
    author=get_user_model()
    created_date = models.DateTimeField('date created')
    published_date = models.DateTimeField('date published')
