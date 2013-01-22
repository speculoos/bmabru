# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table(u'media_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('path', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'media', ['Resource'])

        # Adding model 'Category'
        db.create_table(u'media_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'media', ['Category'])

        # Adding model 'Page'
        db.create_table(u'media_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'media', ['Page'])

        # Adding M2M table for field resources on 'Page'
        db.create_table(u'media_page_resources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'media.page'], null=False)),
            ('resource', models.ForeignKey(orm[u'media.resource'], null=False))
        ))
        db.create_unique(u'media_page_resources', ['page_id', 'resource_id'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table(u'media_resource')

        # Deleting model 'Category'
        db.delete_table(u'media_category')

        # Deleting model 'Page'
        db.delete_table(u'media_page')

        # Removing M2M table for field resources on 'Page'
        db.delete_table('media_page_resources')


    models = {
        u'media.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'media.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['media.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['media.Resource']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'media.resource': {
            'Meta': {'object_name': 'Resource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['media']