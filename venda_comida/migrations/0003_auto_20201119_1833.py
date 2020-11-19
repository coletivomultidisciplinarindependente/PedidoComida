# Generated by Django 3.1.3 on 2020-11-19 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venda_comida', '0002_auto_20201119_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='produto',
            name='promocao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda_comida.promocao'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='avaliacao',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='avaliacao'),
        ),
    ]