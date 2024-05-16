# Generated by Django 4.2.4 on 2023-09-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirDc', '0004_alter_producto_img_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('descript_producto', models.CharField(max_length=120)),
                ('img_producto', models.ImageField(null=True, upload_to='productos')),
                ('valor_compra', models.IntegerField()),
                ('valor_venta', models.IntegerField()),
                ('activo', models.BooleanField()),
                ('encargado', models.CharField(max_length=30)),
            ],
        ),
    ]
