# Generated by Django 2.2 on 2019-09-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190905_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(max_length=800)),
                ('singkatan', models.CharField(max_length=20)),
                ('file_ongkos_kirim', models.CharField(max_length=800)),
            ],
        ),
    ]