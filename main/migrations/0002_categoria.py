# Generated by Django 2.2.3 on 2022-10-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoriaDescripcion', models.CharField(max_length=45, verbose_name='Descripción')),
                ('categoriaActivo', models.CharField(max_length=1, verbose_name='Estado')),
            ],
        ),
    ]
