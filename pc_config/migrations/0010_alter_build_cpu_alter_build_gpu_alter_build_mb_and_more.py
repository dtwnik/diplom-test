# Generated by Django 4.2.5 on 2023-10-20 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_mb_form_factor'),
        ('pc_config', '0009_alter_build_options_alter_build_gpu_alter_build_mb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='CPU',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.cpu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='GPU',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.gpu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='MB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.mb'),
        ),
        migrations.AlterField(
            model_name='build',
            name='PSU',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.psu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='Ram',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.ram'),
        ),
        migrations.AlterField(
            model_name='build',
            name='Storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.storage'),
        ),
    ]
