# Generated by Django 4.1.2 on 2022-10-26 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_image_url_project_url_alter_project_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='project',
            name='id_area',
            field=models.ForeignKey(db_column='id_area', on_delete=django.db.models.deletion.DO_NOTHING, to='projects.area'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_url',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=400),
        ),
    ]
