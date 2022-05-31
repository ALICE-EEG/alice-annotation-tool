# Generated by Django 3.1.3 on 2020-12-27 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_app', '0005_auto_20201227_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetDownloadItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_actual', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='downloads')),
                ('version', models.CharField(default='NA', max_length=128)),
                ('uploaded_dt', models.DateTimeField(auto_now=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data_app.dataset')),
            ],
        ),
    ]