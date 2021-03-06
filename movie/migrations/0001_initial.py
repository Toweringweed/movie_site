# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Malist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField()),
                ('art_type', models.IntegerField()),
                ('art_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_area', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Martist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_id', models.IntegerField(default=-1, unique=True)),
                ('art_name', models.CharField(max_length=100)),
                ('art_info', models.CharField(max_length=1000)),
                ('art_intro', models.CharField(max_length=8000)),
                ('art_award', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Mclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_class', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField(default=-1, unique=True)),
                ('m_name', models.CharField(max_length=80, verbose_name='电影名称')),
                ('m_name2', models.CharField(default='无', max_length=80)),
                ('m_other_name', models.CharField(default='无', max_length=100)),
                ('m_lan', models.CharField(default='无', max_length=50)),
                ('m_zimu', models.CharField(default='无', max_length=30)),
                ('m_file_format', models.CharField(default='无', max_length=30)),
                ('m_file_size', models.CharField(default='无', max_length=30)),
                ('m_size', models.CharField(default='无', max_length=30)),
                ('m_time', models.CharField(default='无', max_length=30)),
                ('m_download', models.CharField(default='无', max_length=1000)),
                ('m_douban_rating', models.FloatField(blank=True, null=True)),
                ('m_douban_voters', models.IntegerField(blank=True, null=True)),
                ('m_douban_url', models.CharField(max_length=100)),
                ('m_imdb_rating', models.FloatField(blank=True, null=True)),
                ('m_imdb_voters', models.IntegerField(blank=True, null=True)),
                ('m_imdb_serial', models.CharField(default='无', max_length=20)),
                ('m_imdb_url', models.CharField(default='无', max_length=100)),
                ('m_poster', models.CharField(default='无', max_length=150)),
                ('m_first_play', models.CharField(default='无', max_length=200)),
                ('m_runtime', models.CharField(default='无', max_length=50)),
                ('m_summary', models.CharField(default='无', max_length=3000)),
                ('m_award', models.CharField(default='无', max_length=1500)),
                ('m_comment_short', models.CharField(default='无', max_length=3000)),
                ('m_comment_rating', models.CharField(default='无', max_length=200)),
                ('m_season', models.IntegerField(blank=True, null=True)),
                ('m_jishu', models.IntegerField(blank=True, null=True)),
                ('m_time_ji', models.IntegerField(blank=True, null=True)),
                ('m_update', models.DateTimeField(auto_now=True)),
                ('m_update_douban', models.DateTimeField(blank=True, null=True)),
                ('m_update_piaohua', models.DateTimeField(blank=True, null=True)),
                ('m_area', models.ManyToManyField(to='movie.Marea')),
                ('m_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Mclass')),
            ],
        ),
        migrations.CreateModel(
            name='Mtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_tag', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Myear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_year', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='mdetail',
            name='m_tag',
            field=models.ManyToManyField(to='movie.Mtag'),
        ),
        migrations.AddField(
            model_name='mdetail',
            name='m_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Myear'),
        ),
    ]
