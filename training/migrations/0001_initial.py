# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fichas'
        db.create_table(u'training_fichas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aluno', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'fichas', to=orm['auth.User'])),
            ('objetivo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_fim', self.gf('django.db.models.fields.DateTimeField')()),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'training', ['Fichas'])

        # Adding model 'TiposTreino'
        db.create_table(u'training_tipostreino', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'training', ['TiposTreino'])

        # Adding model 'Treinos'
        db.create_table(u'training_treinos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'treinos', to=orm['training.Fichas'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo_treino', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'treino', to=orm['training.TiposTreino'])),
            ('volume', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'training', ['Treinos'])

        # Adding model 'NomesExercicio'
        db.create_table(u'training_nomesexercicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('musculo', self.gf('django.db.models.fields.IntegerField')()),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'training', ['NomesExercicio'])

        # Adding model 'ExerciciosAluno'
        db.create_table(u'training_exerciciosaluno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('treino', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'exercicios', to=orm['training.Treinos'])),
            ('nome', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'exerciciosaluno', to=orm['training.NomesExercicio'])),
            ('serie', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('repeticao', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'training', ['ExerciciosAluno'])


    def backwards(self, orm):
        # Deleting model 'Fichas'
        db.delete_table(u'training_fichas')

        # Deleting model 'TiposTreino'
        db.delete_table(u'training_tipostreino')

        # Deleting model 'Treinos'
        db.delete_table(u'training_treinos')

        # Deleting model 'NomesExercicio'
        db.delete_table(u'training_nomesexercicio')

        # Deleting model 'ExerciciosAluno'
        db.delete_table(u'training_exerciciosaluno')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'training.exerciciosaluno': {
            'Meta': {'object_name': 'ExerciciosAluno'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'exerciciosaluno'", 'to': u"orm['training.NomesExercicio']"}),
            'repeticao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'treino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'exercicios'", 'to': u"orm['training.Treinos']"})
        },
        u'training.fichas': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'Fichas'},
            'aluno': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fichas'", 'to': u"orm['auth.User']"}),
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_fim': ('django.db.models.fields.DateTimeField', [], {}),
            'data_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objetivo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'training.nomesexercicio': {
            'Meta': {'object_name': 'NomesExercicio'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'musculo': ('django.db.models.fields.IntegerField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'training.tipostreino': {
            'Meta': {'ordering': "['tipo']", 'object_name': 'TiposTreino'},
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'training.treinos': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'Treinos'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'treinos'", 'to': u"orm['training.Fichas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_treino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'treino'", 'to': u"orm['training.TiposTreino']"}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['training']