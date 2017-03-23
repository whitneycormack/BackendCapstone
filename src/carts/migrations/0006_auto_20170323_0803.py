# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20170323_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='items',
            new_name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=10.0, max_digits=50, decimal_places=2),
        ),
    ]
