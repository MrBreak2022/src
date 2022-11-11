# Generated by Django 4.1.1 on 2022-11-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientmgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.CharField(blank=True, choices=[('Supplier', 'Supplier'), ('Customer', 'Customer')], default='', max_length=50, null=True, verbose_name='Client Name:'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Client Name:'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_number',
            field=models.IntegerField(blank=True, max_length='10', null=True, verbose_name='Contact Number:'),
        ),
    ]
