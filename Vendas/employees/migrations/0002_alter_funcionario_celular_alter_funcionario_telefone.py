# Generated by Django 4.2.6 on 2023-11-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='celular',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]