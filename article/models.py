from time import time
from django.db import models


def get_upload_file_name(instance, filename):
    return "media/files/%s_%s" % (str(time()).replace(".", "_"), filename)


def get_upload_image_file_name(instance, filename):
    return "media/images/%s_%s" % (str(time()).replace(".", "_"), filename)


class Author(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(blank=False)
    likes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=20, blank=False)

    def get_absolute_url(self):
        return '/%s/' % self.title

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.FileField(upload_to=get_upload_file_name, verbose_name="File", blank=True)
    image = models.ImageField(upload_to=get_upload_image_file_name, verbose_name="Image", blank=False)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['publish_date']


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return u'%s' % self.name
