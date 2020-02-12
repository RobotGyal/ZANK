# Generated by Django 3.0 on 2020-02-10 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Code title.', max_length=60)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this code.Computer Generated.', max_length=60)),
                ('description', models.TextField(help_text='Full text of the code.')),
                ('date_posted', models.DateTimeField(verbose_name='date published')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.')),
                ('last_revised', models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.')),
                ('can_dos', models.TextField(help_text="List of do's associated with this code.")),
                ('cannot_dos', models.TextField(help_text="List of don'ts associated with this code.")),
                ('posted_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.ArchitectOrOfficer')),
            ],
        ),
    ]
