# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PartnershipType'
        db.create_table(u'bmabru_partnershiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['PartnershipType'])

        # Adding model 'Partnership'
        db.create_table(u'bmabru_partnership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ptype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.PartnershipType'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.Partner'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.Project'])),
        ))
        db.send_create_signal(u'bmabru', ['Partnership'])

        # Removing M2M table for field partners on 'Project'
        db.delete_table('bmabru_project_partners')


    def backwards(self, orm):
        # Deleting model 'PartnershipType'
        db.delete_table(u'bmabru_partnershiptype')

        # Deleting model 'Partnership'
        db.delete_table(u'bmabru_partnership')

        # Adding M2M table for field partners on 'Project'
        db.create_table(u'bmabru_project_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('partner', models.ForeignKey(orm[u'bmabru.partner'], null=False))
        ))
        db.create_unique(u'bmabru_project_partners', ['project_id', 'partner_id'])


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
        u'bmabru.partnership': {
            'Meta': {'object_name': 'Partnership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Partner']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Project']"}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.PartnershipType']"})
        },
        u'bmabru.partnershiptype': {
            'Meta': {'object_name': 'PartnershipType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'bmabru.partnertype': {
            'Meta': {'object_name': 'PartnerType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.PartnerType']", 'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['bmabru']