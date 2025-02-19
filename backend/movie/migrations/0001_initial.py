# Generated by Django 5.1.5 on 2025-01-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('poster', models.ImageField(upload_to='upload/poster/')),
                ('genre', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
