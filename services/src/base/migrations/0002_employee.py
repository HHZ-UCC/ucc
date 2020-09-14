# Generated by Django 3.0.8 on 2020-07-20 21:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('external_id', models.CharField(max_length=250, unique=True)),
                ('lastname', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=250)),
            ],
        ),
    ]
