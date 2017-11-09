# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


'''
    Base Account model that extends built-in Django User model.
    This model serves as the parent for other account models and is not
    meant to be used directly.
'''
class BaseUser(AbstractUser):
    # account type
    UNKNOWN_TYPE = 'U'
    MAIN_USER_TYPE = 'M'


    USER_TYPE_OPTIONS = (
        (UNKNOWN_TYPE, 'Unknown'),
        (MAIN_USER_TYPE, 'Main User')
    )

    REQUIRED_FIELDS = ["email", "phone_number", "first_name", "last_name"]

    phone_number = models.CharField(max_length=16, unique=True)
    _user_type   = models.CharField(max_length=1, choices=USER_TYPE_OPTIONS, default=UNKNOWN_TYPE)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)


'''
    Main user model that extends BaseUser model.
'''
class MainUser(BaseUser):
    class Meta:
        verbose_name_plural = 'main users'

    def save(self, *args, **kwargs):
        self._user_type = BaseUser.MAIN_USER_TYPE
        super(Customer, self).save(*args, **kwargs)