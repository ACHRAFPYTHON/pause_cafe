# Generated by Django 4.0.1 on 2022-03-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boissonschaudes',
            name='desceription',
            field=models.TextField(default='', max_length=200),
        ),
    ]