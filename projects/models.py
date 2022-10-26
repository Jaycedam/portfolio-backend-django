from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    image_url = models.CharField(max_length=400)
    about = models.TextField(max_length=400)
    id_area = models.ForeignKey('Area', models.DO_NOTHING, db_column='id_area')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"
        ordering = ['id']


class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "area"