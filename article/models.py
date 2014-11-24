from time import time
from django.db import models


def get_upload_file_name(instance, filename):
    return "uploaded_file/%s_%s" % (str(time()).replace(".", "_"), filename)


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.name