# Generated by Django 4.2.6 on 2023-11-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static_img/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static_img/products_photo/%Y/%m/%d'),
        ),
    ]
