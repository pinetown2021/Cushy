# Generated by Django 2.2.2 on 2019-11-03 13:44

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('grocery', '0003_auto_20191026_1727'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Brand',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='company',
            new_name='brand',
        ),
    ]
