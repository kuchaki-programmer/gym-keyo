# Generated by Django 5.0.2 on 2024-03-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
