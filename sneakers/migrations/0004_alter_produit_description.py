# Generated by Django 4.0.2 on 2022-03-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0003_alter_produit_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
