# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

import os
from cStringIO import StringIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from PIL import Image
import piexif

import uuid


def item_upload_path(instance, filename):
    return ("items/%s_%s" % (uuid.uuid1(), filename))


def make_thumbnail(image_filename, thumbnail_obj, crop_square=True):
    """
    Create and save the thumbnail for the photo (simple resize with PIL).
    """
    image_folder, image_name = os.path.split(image_filename)
    thumb_name, thumb_extension = os.path.splitext(image_name)
    thumb_filename = thumb_name + '_thumb' + thumb_extension.lower()

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        print ("\033[31minvalid image extension for %s\033[0m" % image_name)
        return False

    return_status = True
    fh = storage.open(image_filename, 'r')
    try:
        image = Image.open(fh)

        try:
            # load exif data
            exif_dict = piexif.load(image.info["exif"])
            exif_bytes = piexif.dump(exif_dict)
        except:
            exif_bytes = None

        if crop_square: # crop the image so that the resulting thumbnail is a square
            # crop_box = (x, y, width, height)
            if image.size[0] > image.size[1]: # image is wide
                crop_margin = (image.size[0] - image.size[1]) / 2
                crop_box = (crop_margin, 0, image.size[0] - crop_margin, image.size[1])
            elif image.size[1] > image.size[0]: # image is high
                crop_margin = (image.size[1] - image.size[0]) / 2
                crop_box = (0, crop_margin, image.size[0], image.size[1] - crop_margin)
            image = image.crop(crop_box)

        image.thumbnail(settings.THUMB_SIZE, Image.ANTIALIAS)

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = StringIO()
        if exif_bytes:
            image.save(temp_thumb, FTYPE, exif=exif_bytes)
        else:
            image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        thumbnail_obj.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()
    except:
        return_status = False
    finally:
        fh.close()
        return return_status


