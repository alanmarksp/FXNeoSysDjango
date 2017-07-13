# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funds', models.DecimalField(decimal_places=2, default=10000.0, max_digits=12)),
                ('realized_profit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trading_accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
