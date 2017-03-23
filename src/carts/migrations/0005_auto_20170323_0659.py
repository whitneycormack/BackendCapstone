# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cartitem_line_item_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='items',
        ),
    ]
