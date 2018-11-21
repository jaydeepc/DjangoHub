# Generated by Django 2.0.3 on 2018-10-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('user_firstname', models.CharField(max_length=25)),
                ('user_lastname', models.CharField(max_length=25)),
                ('git_username', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=25)),
                ('office', models.CharField(max_length=25)),
                ('user_photo', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='RepoDetails',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('vcs_url', models.CharField(max_length=500)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_techstack', models.CharField(max_length=25)),
            ],
        ),
    ]