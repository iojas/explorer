# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class ProjectImage(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   image = models.ImageField()