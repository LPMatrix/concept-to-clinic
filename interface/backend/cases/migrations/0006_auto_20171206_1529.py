# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-06 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20171204_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casecomparison',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='casepleuralspaces',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='clinicalinformation',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='examparameters',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='extrainformation',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='heartfindings',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='lungsfindings',
            name='COPD',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'MILD'), (2, 'MODERATE'), (3, 'SEVERE')], help_text='Term used to describe progressive lung diseases; describes the degree of COPD progress'),
        ),
        migrations.AlterField(
            model_name='lungsfindings',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='otherfindings',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
        migrations.AlterField(
            model_name='technicalparameters',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cases.Case'),
        ),
    ]