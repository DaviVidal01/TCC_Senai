# Generated by Django 4.2.6 on 2023-11-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0009_alter_marca_bd_marca_alter_tecido_bd_tecido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos_bd',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
