# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0002_auto_20151220_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='status',
            field=models.CharField(default='draft', max_length=15),
        ),
    ]
