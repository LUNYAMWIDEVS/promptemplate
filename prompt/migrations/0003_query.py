# Generated by Django 4.2.7 on 2023-11-24 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prompt', '0002_toneofvoice_prompt_product_prompt_tone_of_voice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('query', models.TextField()),
                ('prompt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prompt.prompt')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]