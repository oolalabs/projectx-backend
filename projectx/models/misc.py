# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



'''
    Model representing a location
'''
class Location(models.Model):
	name = models.CharField(max_length=128)
	geo_long = models.FloatField()
	geo_lat = models.FloatField()
