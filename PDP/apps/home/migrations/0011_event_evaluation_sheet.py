# Generated by Django 5.0.6 on 2024-05-15 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_evaluation_delete_avaliação'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evaluation_sheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.evaluation'),
        ),
    ]