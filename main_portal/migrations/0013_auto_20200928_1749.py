# Generated by Django 3.0.6 on 2020-09-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_portal', '0012_auto_20200714_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='Designation',
            field=models.CharField(max_length=25),
        ),
    ]
