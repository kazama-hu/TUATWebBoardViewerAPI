# Generated by Django 2.0.3 on 2018-03-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180321_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='administrator',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]