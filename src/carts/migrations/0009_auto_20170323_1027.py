# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_auto_20170323_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
