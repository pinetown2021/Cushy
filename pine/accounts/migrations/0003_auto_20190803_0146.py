# Generated by Django 2.2.1 on 2019-08-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190803_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
