# Generated by Django 4.1.5 on 2023-01-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('big', '0003_bob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bob',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
