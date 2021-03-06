# Generated by Django 3.1.3 on 2021-11-05 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0009_annotation_updated_dt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icacomponent',
            old_name='subject',
            new_name='subject_name',
        ),
        migrations.AlterUniqueTogether(
            name='icacomponent',
            unique_together={('name', 'subject_name', 'dataset')},
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subjects', to='data_app.dataset')),
            ],
        ),
    ]
