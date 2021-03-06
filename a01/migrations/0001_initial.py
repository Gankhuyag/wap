# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 21:26
from __future__ import unicode_literals

import a01.models
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('seats', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(400)])),
                ('bseats', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]), size=2), blank=True, null=True, size=20)),
            ],
            bases=(models.Model, a01.models.ToJson),
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('capacity', models.PositiveIntegerField(default=400)),
            ],
            bases=(models.Model, a01.models.ToJson),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=None)),
                ('runtime', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('img', models.ImageField(upload_to='movies/')),
                ('yurl', models.URLField(blank=True, max_length=500, null=True)),
            ],
            bases=(models.Model, a01.models.ToJson),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnum', models.CharField(max_length=30)),
                ('expdate', models.DateField()),
                ('startdate', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a01.Customer')),
            ],
            bases=(models.Model, a01.models.ToJson),
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.TimeField()),
                ('sdate', models.DateField()),
                ('seats', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]), size=20), blank=True, null=True, size=20)),
                ('totalcustomer', models.PositiveIntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a01.Hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a01.Movie')),
            ],
            bases=(models.Model, a01.models.ToJson),
        ),
        migrations.AddField(
            model_name='customer',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a01.Screening'),
        ),
    ]
