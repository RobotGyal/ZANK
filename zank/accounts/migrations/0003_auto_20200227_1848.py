# Generated by Django 3.0.3 on 2020-02-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200211_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architectorofficer',
            name='is_officer',
            field=models.BooleanField(default=False, help_text='How will you use ZANK?'),
        ),
    ]
