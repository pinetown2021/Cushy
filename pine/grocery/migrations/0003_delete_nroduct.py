# Generated by Django 2.2.2 on 2019-12-25 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_nroduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nroduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
