from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
