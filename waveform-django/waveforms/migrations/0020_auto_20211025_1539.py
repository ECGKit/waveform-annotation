# Generated by Django 2.2.13 on 2021-10-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waveforms', '0019_auto_20211019_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='down_sample',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='down_sample_ekg',
            field=models.IntegerField(default=1),
        ),
    ]
