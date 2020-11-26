# Generated by Django 3.1.3 on 2020-11-24 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('code', models.TextField(verbose_name='código')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
        ),
    ]
