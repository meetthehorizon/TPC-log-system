# Generated by Django 4.1 on 2023-11-02 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='priority',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField()),
                ('shortlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.shortlist')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]