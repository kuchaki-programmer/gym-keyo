# Generated by Django 5.0.2 on 2024-02-27 19:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_alter_comment_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='TrainerComment',
        ),
    ]
