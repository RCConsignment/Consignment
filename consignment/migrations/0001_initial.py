# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('damages', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=100)),
                ('num_pieces', models.IntegerField()),
                ('price_1', models.DecimalField(max_digits=7, decimal_places=2)),
                ('price_2', models.DecimalField(max_digits=7, decimal_places=2)),
                ('brand_name', models.ForeignKey(to='consignment.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone number')),
                ('address_street', models.CharField(max_length=500)),
                ('address_city', models.CharField(max_length=500)),
                ('address_state', models.CharField(max_length=2)),
                ('address_country', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=200, verbose_name='paypal email')),
                ('active', models.BooleanField(verbose_name='Is Active?')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(to='consignment.Seller'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(to='consignment.ItemStatus'),
        ),
    ]
