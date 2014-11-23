from article.models import Article
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publish_date')
    search_fields = ('title', 'content')
    list_filter = ('publish_date',)
    ordering = ('-publish_date',)


admin.site.register(Article, ArticleAdmin)