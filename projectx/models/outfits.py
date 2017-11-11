# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from projectx.models.users import MainUser


'''
    Model representing an outfit of a user in the app
'''
class Outfit(models.Model):
	user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)