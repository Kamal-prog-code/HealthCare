# Generated by Django 3.1.3 on 2020-12-04 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.IntegerField(default=0)),
                ('Glucose', models.IntegerField(default=0)),
                ('BP', models.IntegerField(default=0)),
                ('Skinthickness', models.IntegerField(default=0)),
                ('Insulin', models.IntegerField(default=0)),
                ('BMI', models.IntegerField(default=0)),
                ('Diabetic_pf', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=10)),
                ('Res', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.users')),
            ],
        ),
    ]
