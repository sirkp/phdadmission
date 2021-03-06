# Generated by Django 2.2 on 2019-07-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_omrsheets'),
    ]

    operations = [
        migrations.CreateModel(
            name='OMRSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_images', models.ImageField(upload_to='omr_sheets/%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.RenameModel(
            old_name='Announcements',
            new_name='Announcement',
        ),
        migrations.DeleteModel(
            name='OMRSheets',
        ),
    ]
