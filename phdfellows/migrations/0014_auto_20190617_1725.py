# Generated by Django 2.2 on 2019-06-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phdfellows', '0013_auto_20190617_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applying_for',
            field=models.CharField(choices=[('', 'Select'), ('PhD', 'PhD'), ('MS', 'MS')], default='Select', max_length=5),
        ),
    ]