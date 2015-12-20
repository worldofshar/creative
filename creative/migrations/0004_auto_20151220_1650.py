# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0003_auto_20151220_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='tag',
            field=models.CharField(max_length=15, default='short'),
        ),
    ]
