# Generated by Django 3.2.5 on 2021-12-10 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_projects_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
