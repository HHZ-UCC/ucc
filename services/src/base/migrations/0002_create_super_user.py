import os
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_ROOT_USER = os.environ.get('DJANGO_ROOT_USER', 'root')
        DJANGO_ROOT_USER_PASSWORD = os.environ.get('DJANGO_ROOT_USER_PASSWORD', 'root')

        superuser = User.objects.create_superuser(
            username=DJANGO_ROOT_USER,
            password=DJANGO_ROOT_USER_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]