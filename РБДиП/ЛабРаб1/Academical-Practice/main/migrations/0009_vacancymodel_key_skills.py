# Generated by Django 5.0.6 on 2024-07-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_employemnt_name_vacancymodel_employment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancymodel',
            name='key_skills',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
