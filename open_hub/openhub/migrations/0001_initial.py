# Generated by Django 2.0.3 on 2018-03-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(max_length=25)),
                ('user_lastname', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('office', models.CharField(max_length=25)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_techstack', models.CharField(max_length=25)),
            ],
        ),
    ]