# Generated by Django 3.2.4 on 2021-06-14 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_mal_requirements_microtask_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mal_requirements',
            name='microtask_category',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='jobs.microtasks'),
        ),
    ]
