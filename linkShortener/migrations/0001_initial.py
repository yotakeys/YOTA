# Generated by Django 3.2.16 on 2022-12-26 03:45

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
            name='Url',
            fields=[
                ('longUrl', models.TextField()),
                ('shortUrl', models.CharField(max_length=30, primary_key=True, serialize=False)),  # noqa: E501
                ('create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),  # noqa: E501
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]