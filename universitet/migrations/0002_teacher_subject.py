# Generated by Django 5.1.1 on 2024-09-23 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universitet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='universitet.subject'),
        ),
    ]
