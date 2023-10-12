# Generated by Django 4.2.4 on 2023-10-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_electionresultdetails_partyname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionSeatsAndParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(blank=True)),
                ('parylogo', models.ImageField(blank=True, upload_to='partylogo')),
                ('partyname', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='electionresultdetails',
            name='partyname',
        ),
        migrations.RemoveField(
            model_name='electionresultdetails',
            name='parylogo',
        ),
        migrations.RemoveField(
            model_name='electionresultdetails',
            name='seats',
        ),
    ]