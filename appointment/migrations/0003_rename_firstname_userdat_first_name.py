# Generated by Django 4.2.6 on 2023-10-27 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_rename_userdata_userdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdat',
            old_name='firstname',
            new_name='first_name',
        ),
    ]