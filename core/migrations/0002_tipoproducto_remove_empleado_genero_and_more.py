# Generated by Django 5.0.6 on 2024-05-26 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='puesto',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='marca',
            name='nombre',
            field=models.CharField(default='Marca Predeterminada', max_length=255),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos/'),
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('añadido_el', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoproducto'),
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='TipoEmpleado',
        ),
        migrations.DeleteModel(
            name='TipoHerramienta',
        ),
    ]