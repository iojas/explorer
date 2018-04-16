# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from datetime import datetime


def user_directory_path(instance, filename):
    # import pdb; pdb.set_trace()
    return 'uploads/{0}/{1}'.format( instance.project.name,
        datetime.now().strftime('%Y%m%d%H%M%S')+'_'+filename
    )


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class ProjectImage(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   image = models.ImageField(upload_to=user_directory_path)