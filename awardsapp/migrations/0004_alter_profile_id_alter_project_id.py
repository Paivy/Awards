# Generated by Django 4.0.5 on 2022-06-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0003_auto_20220613_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
