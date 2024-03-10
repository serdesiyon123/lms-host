from django.apps import AppConfig
from django.conf import settings

class AuthUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_users'
    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import Group

        def save_to_student(sender, **kwargs):
            user = kwargs['instance']
            if kwargs['created']:
                group, ok = Group.objects.get_or_create(name='student')
                group.user_set.add(user)
        post_save.connect(save_to_student, sender=settings.AUTH_USER_MODEL)
