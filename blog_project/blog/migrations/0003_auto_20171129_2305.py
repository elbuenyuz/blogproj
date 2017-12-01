# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171129_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_email',
            field=models.EmailField(max_length=40),
        ),
    ]
