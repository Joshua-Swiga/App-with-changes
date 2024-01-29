from django.db import models
from django.contrib.auth.models import User


# This model defines a table called posts in the database.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    post = models.TextField()

    def __str__(self):
        return self.title


#Posts added from Django's admin pannel
class BlogPost(models.Model):
    title=models.CharField(max_length= 100)
    body=models.TextField()

    def __str__(self):
        return self.title