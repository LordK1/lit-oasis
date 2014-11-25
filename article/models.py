from time import time
from django.db import models


def get_upload_file_name(instance, filename):
    return "uploaded_file/%s_%s" % (str(time()).replace(".", "_"), filename)


class Author(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(blank=False)
    likes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.FileField(upload_to=get_upload_file_name, verbose_name="File", blank=True)
    author = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.name
