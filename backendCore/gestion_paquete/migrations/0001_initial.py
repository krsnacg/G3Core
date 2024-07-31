# Generated by Django 5.0.6 on 2024-07-18 23:31

import django.core.validators
import gestion_solicitud.services
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoControl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('numero_documento', models.CharField(default=gestion_solicitud.services.generate_unique, max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(32), django.core.validators.MaxLengthValidator(32)])),
            ],
            options={
                'verbose_name_plural': 'Documentos de Control',
            },
        ),
    ]
