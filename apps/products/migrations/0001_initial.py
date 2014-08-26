# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'products_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['products.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'products', ['Category'])

        # Adding model 'Shop'
        db.create_table(u'products_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'products', ['Shop'])

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'products', ['Product'])

        # Adding model 'Cost'
        db.create_table(u'products_cost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Shop'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'products', ['Cost'])

        # Adding unique constraint on 'Cost', fields ['product', 'shop']
        db.create_unique(u'products_cost', ['product_id', 'shop_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Cost', fields ['product', 'shop']
        db.delete_unique(u'products_cost', ['product_id', 'shop_id'])

        # Deleting model 'Category'
        db.delete_table(u'products_category')

        # Deleting model 'Shop'
        db.delete_table(u'products_shop')

        # Deleting model 'Product'
        db.delete_table(u'products_product')

        # Deleting model 'Cost'
        db.delete_table(u'products_cost')


    models = {
        u'products.category': {
            'Meta': {'ordering': "['weight', 'title']", 'object_name': 'Category'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': u"orm['products.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'products.cost': {
            'Meta': {'ordering': "['product', 'shop']", 'unique_together': "(('product', 'shop'),)", 'object_name': 'Cost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Shop']"})
        },
        u'products.product': {
            'Meta': {'ordering': "['weight', 'title']", 'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'products.shop': {
            'Meta': {'ordering': "['weight', 'title']", 'object_name': 'Shop'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['products']