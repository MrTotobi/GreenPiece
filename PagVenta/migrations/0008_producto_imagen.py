# Generated by Django 2.2.5 on 2019-12-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagVenta', '0007_auto_20191204_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='', upload_to='../../../static/img'),
            preserve_default=False,
        ),
    ]
