# Generated by Django 2.2 on 2019-09-04 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190904_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lowongankerja',
            old_name='nama',
            new_name='posisi',
        ),
    ]
