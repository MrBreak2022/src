# Generated by Django 4.1.1 on 2022-11-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invmgmt', '0005_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Donut Package #1', 'Donut Package #1'), ('Donut Package #2', 'Donut Package #2'), ('Donut Package #3', 'Donut Package #3'), ('Donut Package #4', 'Donut Package #4')], default='', max_length=50, null=True, verbose_name='Category:'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='set_price',
            field=models.CharField(blank=True, choices=[('PHP 250', 'PHP 250'), ('PHP 500', 'PHP 500'), ('PHP 750', 'PHP 750'), ('PHP 1000', 'PHP 1000')], default='', max_length=50, null=True, verbose_name='Pricing:'),
        ),
    ]
