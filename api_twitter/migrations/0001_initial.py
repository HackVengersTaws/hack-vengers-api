# Generated by Django 3.0.9 on 2020-10-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('bounding_boxes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('hashtags', models.CharField(blank=True, max_length=100, null=True)),
                ('min_hashtags', models.IntegerField(default=0)),
                ('mencions', models.CharField(blank=True, max_length=100, null=True)),
                ('min_mencions', models.IntegerField(default=0)),
                ('keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha_min_creation_user', models.DateField(blank=True, null=True)),
                ('fecha_max_creation_user', models.DateField(blank=True, null=True)),
                ('min_followers', models.IntegerField(default=0)),
                ('min_friends', models.IntegerField(default=0)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('len_min_tweet', models.IntegerField(default=0)),
                ('min_faves', models.IntegerField(default=0)),
                ('min_retweets', models.IntegerField(default=0)),
                ('min_replies', models.IntegerField(default=0)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('texto', models.CharField(max_length=150)),
                ('longuitud', models.IntegerField(default=0)),
                ('hashtags', models.CharField(max_length=250)),
                ('num_hashtags', models.IntegerField(default=0)),
                ('mencions', models.CharField(max_length=250)),
                ('num_mencions', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=3)),
                ('retweet_count', models.IntegerField(default=0)),
                ('favorite_count', models.IntegerField(default=0)),
                ('name_place', models.CharField(max_length=250)),
                ('full_name_place', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('followers', models.IntegerField(default=0)),
                ('friends', models.IntegerField(default=0)),
                ('create_count', models.DateTimeField()),
            ],
        ),
    ]
