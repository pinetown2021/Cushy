# Generated by Django 2.2.2 on 2019-12-26 08:57

from django.db import migrations, models
import django.db.models.deletion
import grocery.models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0007_auto_20191226_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(null=True, upload_to=grocery.models.brand_directory_path, validators=[grocery.models.validate_image], verbose_name='Brand Image'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=grocery.models.category_directory_path, validators=[grocery.models.validate_image], verbose_name='Category Image'),
        ),
        migrations.AddField(
            model_name='shop',
            name='alternate_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(null=True, upload_to=grocery.models.shop_directory_path, validators=[grocery.models.validate_image], verbose_name='Shop Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='free',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='off',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=grocery.models.product_directory_path, validators=[grocery.models.validate_image], verbose_name='Image')),
                ('product_image', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='grocery.Product')),
            ],
        ),
    ]
