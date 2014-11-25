# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'article_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('likes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'article', ['Author'])

        # Deleting field 'Article.thumbnail'
        db.delete_column(u'article_article', 'thumbnail')

        # Adding field 'Article.uploaded_file'
        db.add_column(u'article_article', 'uploaded_file',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding M2M table for field author on 'Article'
        m2m_table_name = db.shorten_name(u'article_article_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'article.article'], null=False)),
            ('author', models.ForeignKey(orm[u'article.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'article_author')

        # Adding field 'Article.thumbnail'
        db.add_column(u'article_article', 'thumbnail',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Article.uploaded_file'
        db.delete_column(u'article_article', 'uploaded_file')

        # Removing M2M table for field author on 'Article'
        db.delete_table(db.shorten_name(u'article_article_author'))


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['article.Author']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'uploaded_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'article.author': {
            'Meta': {'object_name': 'Author'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'article.comment': {
            'Meta': {'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['article']