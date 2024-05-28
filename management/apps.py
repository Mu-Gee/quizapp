from django.apps import AppConfig


from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command

def create_superuser(sender, **kwargs):
    call_command('createsu')

class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'

    def ready(self):
        post_migrate.connect(create_superuser, sender=self)




class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'
