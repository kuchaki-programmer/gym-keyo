# Generated by Django 5.0.2 on 2024-02-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_trainercomment_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainercomment',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
