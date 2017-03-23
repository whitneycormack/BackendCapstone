# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20170323_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=2),
        ),
    ]
