# Generated by Django 4.0.3 on 2022-03-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_noticia_categoria_alter_noticia_cos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[('Política', 'Economia'), ('Social', 'Esports'), ('Opinió', 'Successos')], default='Sense categoria', max_length=999),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='valoracio_mitja',
            field=models.DecimalField(decimal_places=1, default='0', max_digits=2),
        ),
    ]