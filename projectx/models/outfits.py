# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from projectx.models.users import MainUser
from projectx.models.helpers import make_thumbnail, item_upload_path


'''
    Model representing an outfit of a user in the app
'''
class Outfit(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)


class Media(models.Model):
    # media type
    UNKNOWN_TYPE = 'U'
    IMAGE_TYPE = 'I'
    VIDEO_TYPE = 'V'

    MEDIA_TYPE_OPTIONS = (
        (UNKNOWN_TYPE, 'Unknown'),
        (IMAGE_TYPE, 'Image'),
        (VIDEO_TYPE, 'Video'),
    )

    media_type = models.CharField(max_length=1, choices=MEDIA_TYPE_OPTIONS, default=UNKNOWN_TYPE)
    media = models.FileField(upload_to=item_upload_path, null=True, blank=True)
    thumbnail = models.FileField(upload_to=item_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

        # Make and save the thumbnail for the photo here.
        if media_type == IMAGE_TYPE and self.media is not None and self.media.name is not None:
            if (self.thumbnail is None or self.thumbnail.name is None or self.thumbnail.name == ""):
                if not make_thumbnail(self.media.name, self.thumbnail):
                    print("\033[31m;ERROR: Making thumbnail failed. Please check if file type is valid.\033[0m;")
