# Generated by Django 3.1.3 on 2021-11-06 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0012_auto_20211106_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icacomponent',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ics', to='data_app.subject'),
        ),
    ]