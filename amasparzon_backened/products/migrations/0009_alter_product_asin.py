# Generated by Django 3.2.6 on 2021-12-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211224_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='asin',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
