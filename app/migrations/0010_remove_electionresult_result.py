# Generated by Django 4.2.4 on 2023-09-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_electionresultdetails_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electionresult',
            name='Result',
        ),
    ]
