from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import User
from adapters.helpical_adapter import HelpicalAdapter


@receiver(post_save, sender=User)
def customer_creator(sender, instance, created, **kwargs):
    # Your code here
    if not instance.customer_created:
        helpical_adapter = HelpicalAdapter()
        data, is_verified = helpical_adapter.create_customer(user=instance)
        if is_verified:
            instance.helpical_id = data['returned_values'][0]['id']
            instance.helpical_password = data['returned_values'][0]['password']
            instance.customer_created = True
            instance.save()

