from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import ProfileModel

@receiver(post_save, sender=User)
def create_profile(**kwargs):
    if kwargs.get('created'):
        # a Profil táblába jöjjön létre a rekord
        ProfileModel.objects.create(user=kwargs.get('instance'))
        # insert into profile(user, image) values (1, 'path_to_image')
        # CRUD - Create Read Update Delete
        # djangoban: Create - insert, Read - all()

# @receiver(post_save, sender=User)
# def save_profile(**kwargs):
#     kwargs.get('instance').profilemodel.save()