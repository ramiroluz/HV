# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-21 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medcal', '0004_remove_localizacao_cidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localizacao',
            old_name='cidade_fk',
            new_name='cidade',
        ),
    ]