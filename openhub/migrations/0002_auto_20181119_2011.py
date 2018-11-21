# Generated by Django 2.1.3 on 2018-11-19 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openhub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributors',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='repodetails',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='repodetails',
            name='cid',
        ),
        migrations.AddField(
            model_name='repodetails',
            name='contributor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='openhub.Contributors'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_photo',
            field=models.ImageField(blank=True, default='profile_image/default.png', upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='repodetails',
            name='project_techstack',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterModelTable(
            name='contributors',
            table='openhub_contributors',
        ),
        migrations.AlterModelTable(
            name='repodetails',
            table='openhub_repos',
        ),
    ]
