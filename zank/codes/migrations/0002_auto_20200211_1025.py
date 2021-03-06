# Generated by Django 3.0 on 2020-02-11 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='created',
        ),
        migrations.AlterField(
            model_name='code',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.'),
        ),
        migrations.AlterField(
            model_name='code',
            name='posted_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
