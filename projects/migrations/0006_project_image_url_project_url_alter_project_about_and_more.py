# Generated by Django 4.1.2 on 2022-10-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_area_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
