# Generated by Django 3.1.4 on 2021-06-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_mal_requirements_microtask_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='microtasks',
            name='Quantity_of_the_Job',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mal_requirements',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='microtasks',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mtojobcategories',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
