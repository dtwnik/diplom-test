# Generated by Django 4.2.5 on 2023-09-18 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_mb_m2_sum'),
        ('pc_config', '0004_build_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='Storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.storage'),
        ),
    ]
