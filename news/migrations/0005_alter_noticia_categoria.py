# Generated by Django 4.0.3 on 2022-03-21 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_noticia_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[(1, 'Política'), (2, 'Economia'), (3, 'Social'), (4, 'Esports'), (5, 'Opinió'), (6, 'Successos')], default='Sense categoria', max_length=999),
        ),
    ]