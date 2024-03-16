from account.models import CustomUser
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_title = models.CharField(max_length=25)

    def __str__(self):
        return self.tag_title


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    category = models.ManyToManyField(Category, related_name='blogs')
    published_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogs', null=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')

    def __str__(self):
        return f'{self.title}-{self.published_at}'


class BlogComment(models.Model):
    title = models.CharField(max_length=20)
    comment_description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogcomments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.user}'


