# Generated by Django 2.2 on 2019-06-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phdfellows', '0002_auto_20190612_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_no',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
