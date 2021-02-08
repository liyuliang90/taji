# Generated by Django 3.1.6 on 2021-02-04 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('tower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tower.tower')),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('excel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tower.excel')),
            ],
        ),
    ]