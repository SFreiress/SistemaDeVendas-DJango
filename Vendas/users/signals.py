from django.db.models.signals import post_migrate
from django.dispatch import receiver
from users.models import CustomUser

@receiver(post_migrate)
def create_default_user(**kwargs):
    if not CustomUser.objects.filter(email='admin@admin.com').exists():
        CustomUser.objects.create_superuser('admin',
                        password='admin', email='admin@admin.com')
