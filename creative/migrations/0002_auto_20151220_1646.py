# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='content',
            field=models.TextField(max_length=100000),
        ),
    ]
