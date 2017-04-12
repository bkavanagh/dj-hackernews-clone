from django.db import models
from django.contrib.auth.models import User


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "TimeStamp"
        verbose_name_plural = "TimeStamps"
        abstract = True


class Post(TimeStamp):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey('Author')
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title
