# Generated by Django 4.0.3 on 2022-03-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='color',
            field=models.CharField(default='white', max_length=20),
        ),
        migrations.AddField(
            model_name='furniture',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
