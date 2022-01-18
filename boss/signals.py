from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from django.dispatch import receiver
from .models import agent

# @receiver(post_save, sender=User)
def create_agent(sender, instance, created, **kwargs):
    if created:
        agent.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
        )
        print('prfile created')

post_save.connect(create_agent, sender=User)
