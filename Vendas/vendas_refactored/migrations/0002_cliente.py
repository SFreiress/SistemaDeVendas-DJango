# Generated by Django 4.2.6 on 2023-10-30 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vendas_refactored', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('numero', models.IntegerField(max_length=6)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
    ]
