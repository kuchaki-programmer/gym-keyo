# Generated by Django 5.0.2 on 2024-02-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_trainer_instagram_id_alter_trainer_linkedin_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='about_trainer',
            field=models.TextField(default=''),
        ),
    ]
