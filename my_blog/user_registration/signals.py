from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import ProfileModel

@receiver(post_save, sender=User)
def create_profile(**kwargs):
    with open('create_profile.txt', 'w', encoding="utf-8") as f:
        f.write(str(kwargs))
    print(kwargs)
    print('létrejött a user')