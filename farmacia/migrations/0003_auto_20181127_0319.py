# Generated by Django 2.1.2 on 2018-11-27 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0002_auto_20181126_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='id_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='id_medicamento',
            new_name='medicamento',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='producto',
        ),
        migrations.AddField(
            model_name='compras',
            name='medicamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='farmacia.Medicamento'),
            preserve_default=False,
        ),
    ]
