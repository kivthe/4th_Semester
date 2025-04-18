# Generated by Django 5.0.6 on 2024-07-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_vacancymodel_data_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancymodel',
            name='alternate_url',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancymodel',
            name='salary_currency',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancymodel',
            name='salary_gross',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancymodel',
            name='salary_max',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancymodel',
            name='salary_min',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancymodel',
            name='url',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
