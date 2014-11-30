from article.models import Article, Comment, Author, Category
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publish_date')
    search_fields = ('title', 'content')
    list_filter = ('publish_date',)
    ordering = ('-publish_date',)
    filter_horizontal = ('author', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'publish_date', 'article')
    search_fields = ('name', 'body', 'article')
    list_filter = ('publish_date',)
    ordering = ('-publish_date',)
    fields = ('name', 'body', 'article')
    list_display_links = ('article',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'likes')
    search_fields = ('name', 'email_address')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)