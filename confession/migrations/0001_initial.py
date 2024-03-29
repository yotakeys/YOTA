# Generated by Django 4.1.5 on 2023-07-22 13:48

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
            name='Confession',
            fields=[
                ('slug', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=30)),
                ('target', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('answer', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ("I don't know what to say", "I don't know what to say"), ('I Will Think About It', 'I Will Think About It')], max_length=30)),
                ('response', models.TextField(blank=True, null=True)),
                ('is_answerred', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('answer_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]
