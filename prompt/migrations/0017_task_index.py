# Generated by Django 5.0.6 on 2024-06-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prompt', '0016_baton_endpoint_department_baton_endpoints_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]