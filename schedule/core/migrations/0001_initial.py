# Generated by Django 5.0.6 on 2024-05-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]