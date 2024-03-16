from account.models import CustomUser
from django.db import models

class SportActivity(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class JobPosition(models.Model):
    sport_activity = models.ForeignKey(SportActivity, on_delete=models.CASCADE, related_name='job_positions')
    grade = models.CharField(max_length=100)
    duty = models.TextField()

    def __str__(self):
        return f'{self.sport_activity}-{self.grade}'


class Trainer(models.Model):
    full_name = models.CharField(max_length=200)
    job_position = models.ManyToManyField(JobPosition, related_name='trainers')
    age = models.SmallIntegerField()
    about_trainer = models.TextField(default='')
    image = models.ImageField(null=True, upload_to='trainer')
    instagram_id = models.CharField(max_length=300, default='#', blank=True)
    twitter_id = models.CharField(max_length=300, default='#', blank=True)
    linkedin_id = models.CharField(max_length=300, default='#', blank=True)


    def __str__(self):
        return f'{self.full_name}'


class TrainerComment(models.Model):
    title = models.CharField(max_length=30, null=True)
    comment_description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='comments')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.user.username}'


