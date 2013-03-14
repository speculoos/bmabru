# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubjectiveImage'
        db.create_table(u'media_subjectiveimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_width', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('image_height', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'media', ['SubjectiveImage'])


    def backwards(self, orm):
        # Deleting model 'SubjectiveImage'
        db.delete_table(u'media_subjectiveimage')


    models = {
        u'bmabru.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.ProjectStatus']"}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'sentence_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sentence_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'bmabru.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'bmabru.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'bmabru.mission': {
            'Meta': {'object_name': 'Mission'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'bmabru.partner': {
            'Meta': {'object_name': 'Partner'},
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners'", 'to': u"orm['bmabru.PartnerType']"}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'bmabru.partnertype': {
            'Meta': {'object_name': 'PartnerType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'bmabru.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'bmabru.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'bmabru.project': {
            'Meta': {'object_name': 'Project'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Action']", 'symmetrical': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.City']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'functions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Function']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.ProjectImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Mission']", 'blank': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Partner']", 'symmetrical': 'False'}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Procedure']"}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Program']", 'symmetrical': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'None'", 'max_length': '255'}),
            'steps': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Step']", 'symmetrical': 'False'}),
            'surface': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '64', 'blank': 'True'})
        },
        u'bmabru.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'zoom_level': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'bmabru.projectstatus': {
            'Meta': {'object_name': 'ProjectStatus'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'bmabru.step': {
            'Meta': {'object_name': 'Step'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'media.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'media.featured': {
            'Meta': {'ordering': "['order']", 'object_name': 'Featured'},
            'ftype': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['media.Page']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Project']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'media.page': {
            'Meta': {'ordering': "['order']", 'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['media.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['media.Resource']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'title_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'media.resource': {
            'Meta': {'object_name': 'Resource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'media.subjectiveimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'SubjectiveImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        }
    }

    complete_apps = ['media']