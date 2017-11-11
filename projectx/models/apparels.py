# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from projectx.models.outfits import Media
from projectx.models.misc import Location



'''
    Model representing the type of an apparel
'''
class ApparelType(models.Model):
	name = models.CharField(max_length=128)


'''
    Model representing an apparel 
'''
class Apparel(models.Model):
	name = models.CharField(max_length=128)
	apparel_type = models.ForeignKey(ApparelType, on_delete=models.PROTECT)
	price = models.FloatField()
	online = models.BooleanField()
	link = models.CharField(max_length=128)
	location = models.ForeignKey(Location, on_delete=models.PROTECT)


'''
    Model representing the link between a media and an apparel
'''
class ApparelTag(models.Model):
	apparel = models.ForeignKey(Apparel, on_delete=models.CASCADE)
	media = models.ForeignKey(Media, on_delete=models.CASCADE)
	x_coord = models.FloatField()
	y_coord = models.FloatField()