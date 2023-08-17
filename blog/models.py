from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=12)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    edited = models.BooleanField(default=False)
