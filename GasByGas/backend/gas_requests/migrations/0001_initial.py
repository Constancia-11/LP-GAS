# Generated by Django 5.1.7 on 2025-03-20 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outlets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('token', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outlets.outlet')),
            ],
        ),
    ]
