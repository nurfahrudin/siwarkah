# Generated by Django 2.0 on 2019-07-11 22:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
import warkah.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=3, unique=True)),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=6, unique=True)),
                ('nama', models.CharField(max_length=50)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warkah.Kecamatan')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('departemen', models.CharField(max_length=100)),
                ('bidang', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime.today)),
                ('update_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warkah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_subjek', models.CharField(max_length=128)),
                ('no_berkas', models.CharField(max_length=4)),
                ('tahun', models.IntegerField()),
                ('document', models.FileField(max_length=500, upload_to=warkah.models.upload_dest)),
                ('create_date', models.DateTimeField(default=datetime.datetime.today)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warkah.Kecamatan')),
                ('kelurahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warkah.Kelurahan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warkah.User')),
            ],
        ),
    ]