# Generated by Django 3.1 on 2020-09-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20200904_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='mode',
            field=models.CharField(choices=[('1', 'Draft'), ('2', 'Published')], default='Draft', max_length=10),
        ),
    ]