from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

"""
Model lefejlesztve -> python manage.py makemigrations -> python manage.py migrate
"""

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    date_posted = models.DateTimeField(default=timezone.now) #referencia hivatkozás
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f"{self.author}_{self.title.split(' ')[0]}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})