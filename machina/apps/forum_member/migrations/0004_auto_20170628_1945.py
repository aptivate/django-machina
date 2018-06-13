# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-28 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import machina.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_member', '0003_auto_20160227_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumprofile',
            name='auto_subscribe_topics',
            field=models.BooleanField(default=False, verbose_name='Automatically subscribe to topics you create.'),
        ),
        migrations.AddField(
            model_name='forumprofile',
            name='notify_subscribed_topics',
            field=models.BooleanField(default=False, verbose_name='Receive an email notification on new replies on subscribed topics.'),
        ),
    ]
