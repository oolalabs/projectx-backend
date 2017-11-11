# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from projectx.models.users import MainUser
from projectx.models.outfits import Outfit



'''
    Model representing a like given by a user to an outfit
'''
class Like(models.Model):
	user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
	outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)


'''
    Model representing a comment given by a user to an outfit
'''
class Comment(models.Model):
	user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
	outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)


'''
    Model representing an outfit being saved by a user for later access
'''
class Save(models.Model):
	user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
	outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)