# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from projectx.models.outfits import Outfit



'''
    Model representing a hashtag to be used for filtering
'''
class HashTag(models.Model):
	name = models.CharField(max_length=128)


'''
    Model representing a link between an outfit and a hashtag
'''
class HashTagLink(models.Model):
	outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
	hashtag = models.ForeignKey(HashTag, on_delete=models.CASCADE)




