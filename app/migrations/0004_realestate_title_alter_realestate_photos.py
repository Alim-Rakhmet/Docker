# Generated by Django 4.2.7 on 2023-12-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_leasecontract_realestate_delete_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='realestate',
            name='photos',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]