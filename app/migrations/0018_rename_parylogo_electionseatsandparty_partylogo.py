# Generated by Django 4.2.4 on 2023-10-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_upcommingelectionresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electionseatsandparty',
            old_name='parylogo',
            new_name='partylogo',
        ),
    ]