# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):
    
    initial = True

    dependencies = [
        ('cabotapp', '0003_auto_20170201_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='KafkaAlert',
            fields=[
                ('alertplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cabotapp.AlertPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.alertplugin',),
        )
    ]
