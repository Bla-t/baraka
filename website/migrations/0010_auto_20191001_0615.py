# Generated by Django 2.2 on 2019-10-01 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20191001_0537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabang',
            options={'verbose_name_plural': 'Cabang'},
        ),
        migrations.AlterField(
            model_name='cabang',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Area'),
        ),
    ]
