# Generated by Django 4.2.4 on 2023-09-30 14:56

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_electionresultdetails_margin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electionresult',
            name='Result',
        ),
        migrations.RemoveField(
            model_name='electionresult',
            name='content',
        ),
        migrations.RemoveField(
            model_name='electionresult',
            name='image',
        ),
        migrations.RemoveField(
            model_name='electionresult',
            name='title',
        ),
        migrations.RemoveField(
            model_name='electionresult',
            name='video',
        ),
        migrations.AddField(
            model_name='electionresultdetails',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electionresultdetails',
            name='image',
            field=models.ImageField(default=1, upload_to='pollings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electionresultdetails',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electionresultdetails',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=1),
            preserve_default=False,
        ),
    ]
