# Generated by Django 4.0.2 on 2022-03-05 08:34

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Task name')),
                ('date_of_creating', models.DateTimeField(auto_now_add=True, verbose_name='Date of creating')),
                ('status', models.CharField(choices=[('Created', 'Created'), ('In work', 'In work'), ('Closed', 'Closed')], max_length=10, verbose_name='Status')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='created_tasks')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='executing_tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('text', models.CharField(blank=True, max_length=200, verbose_name='Comment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='tasks.task', verbose_name='Task')),
                ('user', models.ForeignKey(on_delete=models.SET('Unknown user'), related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
