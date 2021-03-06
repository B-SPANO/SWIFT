# Generated by Django 2.1.5 on 2019-01-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190127_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='starship',
            old_name='cost',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='vehicule',
            old_name='cost',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='armor',
            name='defense',
        ),
        migrations.AddField(
            model_name='armor',
            name='defense_close',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='defense HtH'),
        ),
        migrations.AddField(
            model_name='armor',
            name='defense_dist',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='defense distance'),
        ),
    ]
