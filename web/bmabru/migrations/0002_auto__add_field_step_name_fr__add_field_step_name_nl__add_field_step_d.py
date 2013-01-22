# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Step.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_step', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Step.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_step', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Step.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_step', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Step.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_step', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Step.date'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_step', 'date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Program.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_program', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Program.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_program', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Program.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_program', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Program.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_program', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Function.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_function', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Function.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_function', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Function.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_function', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Function.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_function', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Procedure.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_procedure', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Procedure.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_procedure', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Procedure.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_procedure', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Procedure.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_procedure', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'ProjectStatus.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_projectstatus', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'ProjectStatus.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_projectstatus', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'ProjectStatus.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_projectstatus', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'ProjectStatus.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_projectstatus', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Action.sentence_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_action', 'sentence_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Action.sentence_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_action', 'sentence_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Mission.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_mission', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Mission.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_mission', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Mission.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_mission', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Mission.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_mission', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Project.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_project', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Project.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_project', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Project.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_project', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Project.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_project', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding M2M table for field steps on 'Project'
        try:
            db.start_transaction()
            db.create_table(u'bmabru_project_steps', (
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
                ('project', models.ForeignKey(orm[u'bmabru.project'], null=False)),
                ('step', models.ForeignKey(orm[u'bmabru.step'], null=False))
            ))
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
        try:
            db.start_transaction()
            db.create_unique(u'bmabru_project_steps', ['project_id', 'step_id'])
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()

        # Adding field 'Partner.name_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_partner', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Partner.name_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_partner', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Partner.description_fr'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_partner', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass

        # Adding field 'Partner.description_nl'
        try:
            db.start_transaction()
            db.add_column(u'bmabru_partner', 'description_nl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)
            db.commit_transaction()
        except Exception:
            db.rollback_transaction()
            pass


    def backwards(self, orm):
        # Deleting field 'Step.name_fr'
        db.delete_column(u'bmabru_step', 'name_fr')

        # Deleting field 'Step.name_nl'
        db.delete_column(u'bmabru_step', 'name_nl')

        # Deleting field 'Step.description_fr'
        db.delete_column(u'bmabru_step', 'description_fr')

        # Deleting field 'Step.description_nl'
        db.delete_column(u'bmabru_step', 'description_nl')

        # Deleting field 'Step.date'
        db.delete_column(u'bmabru_step', 'date')

        # Deleting field 'Program.name_fr'
        db.delete_column(u'bmabru_program', 'name_fr')

        # Deleting field 'Program.name_nl'
        db.delete_column(u'bmabru_program', 'name_nl')

        # Deleting field 'Program.description_fr'
        db.delete_column(u'bmabru_program', 'description_fr')

        # Deleting field 'Program.description_nl'
        db.delete_column(u'bmabru_program', 'description_nl')

        # Deleting field 'Function.name_fr'
        db.delete_column(u'bmabru_function', 'name_fr')

        # Deleting field 'Function.name_nl'
        db.delete_column(u'bmabru_function', 'name_nl')

        # Deleting field 'Function.description_fr'
        db.delete_column(u'bmabru_function', 'description_fr')

        # Deleting field 'Function.description_nl'
        db.delete_column(u'bmabru_function', 'description_nl')

        # Deleting field 'Procedure.name_fr'
        db.delete_column(u'bmabru_procedure', 'name_fr')

        # Deleting field 'Procedure.name_nl'
        db.delete_column(u'bmabru_procedure', 'name_nl')

        # Deleting field 'Procedure.description_fr'
        db.delete_column(u'bmabru_procedure', 'description_fr')

        # Deleting field 'Procedure.description_nl'
        db.delete_column(u'bmabru_procedure', 'description_nl')

        # Deleting field 'ProjectStatus.name_fr'
        db.delete_column(u'bmabru_projectstatus', 'name_fr')

        # Deleting field 'ProjectStatus.name_nl'
        db.delete_column(u'bmabru_projectstatus', 'name_nl')

        # Deleting field 'ProjectStatus.description_fr'
        db.delete_column(u'bmabru_projectstatus', 'description_fr')

        # Deleting field 'ProjectStatus.description_nl'
        db.delete_column(u'bmabru_projectstatus', 'description_nl')

        # Deleting field 'Action.sentence_fr'
        db.delete_column(u'bmabru_action', 'sentence_fr')

        # Deleting field 'Action.sentence_nl'
        db.delete_column(u'bmabru_action', 'sentence_nl')

        # Deleting field 'Mission.name_fr'
        db.delete_column(u'bmabru_mission', 'name_fr')

        # Deleting field 'Mission.name_nl'
        db.delete_column(u'bmabru_mission', 'name_nl')

        # Deleting field 'Mission.description_fr'
        db.delete_column(u'bmabru_mission', 'description_fr')

        # Deleting field 'Mission.description_nl'
        db.delete_column(u'bmabru_mission', 'description_nl')

        # Deleting field 'Project.name_fr'
        db.delete_column(u'bmabru_project', 'name_fr')

        # Deleting field 'Project.name_nl'
        db.delete_column(u'bmabru_project', 'name_nl')

        # Deleting field 'Project.description_fr'
        db.delete_column(u'bmabru_project', 'description_fr')

        # Deleting field 'Project.description_nl'
        db.delete_column(u'bmabru_project', 'description_nl')

        # Removing M2M table for field steps on 'Project'
        db.delete_table('bmabru_project_steps')

        # Deleting field 'Partner.name_fr'
        db.delete_column(u'bmabru_partner', 'name_fr')

        # Deleting field 'Partner.name_nl'
        db.delete_column(u'bmabru_partner', 'name_nl')

        # Deleting field 'Partner.description_fr'
        db.delete_column(u'bmabru_partner', 'description_fr')

        # Deleting field 'Partner.description_nl'
        db.delete_column(u'bmabru_partner', 'description_nl')


    models = {
        u'bmabru.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bmabru.ProjectStatus']"}),
            'sentence': ('django.db.models.fields.TextField', [], {}),
            'sentence_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sentence_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'budget': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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