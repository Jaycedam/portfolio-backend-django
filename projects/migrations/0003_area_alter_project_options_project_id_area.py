# Generated by Django 4.1.2 on 2022-10-26 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='project',
            name='id_area',
            field=models.ForeignKey(db_column='id_area', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.area'),
        ),
    ]