# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PartnerType'
        db.create_table(u'bmabru_partnertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['PartnerType'])

        # Adding model 'Partner'
        db.create_table(u'bmabru_partner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('ptype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partners', to=orm['bmabru.PartnerType'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('subscribed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128, blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Partner'])

        # Adding model 'Program'
        db.create_table(u'bmabru_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Program'])

        # Adding model 'Procedure'
        db.create_table(u'bmabru_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Procedure'])

        # Adding model 'ProjectImage'
        db.create_table(u'bmabru_projectimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('zoom_level', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['ProjectImage'])

        # Adding model 'Function'
        db.create_table(u'bmabru_function', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Function'])

        # Adding model 'Mission'
        db.create_table(u'bmabru_mission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Mission'])

        # Adding model 'ProjectStatus'
        db.create_table(u'bmabru_projectstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'bmabru', ['ProjectStatus'])

        # Adding model 'Action'
        db.create_table(u'bmabru_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sentence', self.gf('django.db.models.fields.TextField')()),
            ('project_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.ProjectStatus'])),
        ))
        db.send_create_signal(u'bmabru', ['Action'])

        # Adding model 'Step'
        db.create_table(u'bmabru_step', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'bmabru', ['Step'])

        # Adding model 'Project'
        db.create_table(u'bmabru_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('surface', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=64, blank=True)),
            ('budget', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=64, blank=True)),
            ('procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.Procedure'])),
            ('mission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmabru.Mission'], blank=True)),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(geography=True)),
        ))
        db.send_create_signal(u'bmabru', ['Project'])

        # Adding M2M table for field partners on 'Project'
        db.create_table(u'bmabru_project_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('partner', models.ForeignKey(orm[u'bmabru.partner'], null=False))
        ))
        db.create_unique(u'bmabru_project_partners', ['project_id', 'partner_id'])

        # Adding M2M table for field programs on 'Project'
        db.create_table(u'bmabru_project_programs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('program', models.ForeignKey(orm[u'bmabru.program'], null=False))
        ))
        db.create_unique(u'bmabru_project_programs', ['project_id', 'program_id'])

        # Adding M2M table for field functions on 'Project'
        db.create_table(u'bmabru_project_functions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('function', models.ForeignKey(orm[u'bmabru.function'], null=False))
        ))
        db.create_unique(u'bmabru_project_functions', ['project_id', 'function_id'])

        # Adding M2M table for field image on 'Project'
        db.create_table(u'bmabru_project_image', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('projectimage', models.ForeignKey(orm[u'bmabru.projectimage'], null=False))
        ))
        db.create_unique(u'bmabru_project_image', ['project_id', 'projectimage_id'])

        # Adding M2M table for field actions on 'Project'
        db.create_table(u'bmabru_project_actions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
            ('action', models.ForeignKey(orm[u'bmabru.action'], null=False))
        ))
        db.create_unique(u'bmabru_project_actions', ['project_id', 'action_id'])


    def backwards(self, orm):
        # Deleting model 'PartnerType'
        db.delete_table(u'bmabru_partnertype')

        # Deleting model 'Partner'
        db.delete_table(u'bmabru_partner')

        # Deleting model 'Program'
        db.delete_table(u'bmabru_program')

        # Deleting model 'Procedure'
        db.delete_table(u'bmabru_procedure')

        # Deleting model 'ProjectImage'
        db.delete_table(u'bmabru_projectimage')

        # Deleting model 'Function'
        db.delete_table(u'bmabru_function')

        # Deleting model 'Mission'
        db.delete_table(u'bmabru_mission')

        # Deleting model 'ProjectStatus'
        db.delete_table(u'bmabru_projectstatus')

        # Deleting model 'Action'
        db.delete_table(u'bmabru_action')

        # Deleting model 'Step'
        db.delete_table(u'bmabru_step')

        # Deleting model 'Project'
        db.delete_table(u'bmabru_project')

        # Removing M2M table for field partners on 'Project'
        db.delete_table('bmabru_project_partners')

        # Removing M2M table for field programs on 'Project'
        db.delete_table('bmabru_project_programs')

        # Removing M2M table for field functions on 'Project'
        db.delete_table('bmabru_project_functions')

        # Removing M2M table for field image on 'Project'
        db.delete_table('bmabru_project_image')

        # Removing M2M table for field actions on 'Project'
        db.delete_table('bmabru_project_actions')


    models = {
        u'bmabru.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.ProjectStatus']"}),
            'sentence': ('django.db.models.fields.TextField', [], {})
        },
        u'bmabru.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'bmabru.mission': {
            'Meta': {'object_name': 'Mission'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'bmabru.partner': {
            'Meta': {'object_name': 'Partner'},
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'bmabru.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'bmabru.project': {
            'Meta': {'object_name': 'Project'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Action']", 'symmetrical': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'budget': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'functions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Function']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.ProjectImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'mission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Mission']", 'blank': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Partner']", 'symmetrical': 'False'}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.Procedure']"}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bmabru.Program']", 'symmetrical': 'False'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'bmabru.step': {
            'Meta': {'object_name': 'Step'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['bmabru']