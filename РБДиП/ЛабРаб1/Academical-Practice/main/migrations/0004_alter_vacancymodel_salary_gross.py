# Generated by Django 5.0.6 on 2024-07-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_vacancymodel_alternate_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancymodel',
            name='salary_gross',
            field=models.BooleanField(),
        ),
    ]
