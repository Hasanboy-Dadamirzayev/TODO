# Generated by Django 5.2.1 on 2025-05-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('batafsil', models.TextField(blank=True, null=True)),
                ('y_vaqt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
