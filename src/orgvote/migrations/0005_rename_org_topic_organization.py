# Generated by Django 4.2 on 2023-04-26 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgvote', '0004_rename_organization_text_organization_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='org',
            new_name='organization',
        ),
    ]
