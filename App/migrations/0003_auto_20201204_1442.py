# Generated by Django 3.1.2 on 2020-12-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20201204_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabtest',
            name='Res',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='diabtest',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]