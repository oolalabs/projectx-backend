# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.response import Response

from projectx.models import *
from projectx.serializers import *
from projectx.permissions import *


class HashTagViewSet(viewsets.ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializer
    permission_classes = (AllowAnyPermission,)

class HashTagLinkViewSet(viewsets.ModelViewSet):
    queryset = HashTagLink.objects.all()
    serializer_class = HashTagLinkSerializer
    permission_classes = (AllowAnyPermission,)
