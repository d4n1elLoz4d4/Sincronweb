# Generated by Django 2.2.3 on 2022-10-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='Categoria_idCategoria',
            field=models.IntegerField(max_length=11, verbose_name='Categoria'),
        ),
    ]