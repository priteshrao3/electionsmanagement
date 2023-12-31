# Generated by Django 4.2.4 on 2023-09-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_electionresult_ruling_party_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Candidate_Name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Constituency_Name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Level',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Margin',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Party',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='electionresultdetails',
            name='Votes',
            field=models.IntegerField(blank=True),
        ),
    ]
