# Generated by Django 3.2.2 on 2021-06-14 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20210614_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mal_requirements',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mal_requirements',
            name='microtask_category',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='jobs.mtojobcategories'),
        ),
        migrations.AlterField(
            model_name='microtasks',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mtojobcategories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
