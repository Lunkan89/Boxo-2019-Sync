# Generated by Django 2.0.5 on 2019-03-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(blank=True, max_length=150, null=True)),
                ('genre', models.CharField(max_length=150, null=True)),
                ('released', models.CharField(max_length=150, null=True)),
                ('imdb_rating', models.CharField(max_length=150, null=True)),
                ('poster', models.URLField(null=True)),
                ('runtime', models.CharField(max_length=150, null=True)),
                ('trailer', models.URLField(null=True)),
            ],
        ),
    ]
