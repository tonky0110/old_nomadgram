# Generated by Django 2.0.4 on 2018-06-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20180627_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
