# Generated by Django 3.2.6 on 2021-08-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='user_id',
        ),
    ]
