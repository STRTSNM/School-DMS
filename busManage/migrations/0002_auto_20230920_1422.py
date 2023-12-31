# Generated by Django 3.2.21 on 2023-09-20 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='studentlist',
            name='classs',
            field=models.CharField(choices=[('xii', 'XII'), ('xi', 'XI'), ('x', 'X')], default='xii', max_length=100),
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_stops', to='busManage.busroute')),
            ],
        ),
    ]
