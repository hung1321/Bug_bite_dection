# Generated by Django 4.2.7 on 2023-11-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insect', '0009_medic_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medic',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
