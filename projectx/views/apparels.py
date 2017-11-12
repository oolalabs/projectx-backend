# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.response import Response

from projectx.models import *
from projectx.serializers import *
from projectx.permissions import *


class ApparelTypeViewSet(viewsets.ModelViewSet):
    queryset = ApparelType.objects.all()
    serializer_class = ApparelTypeSerializer
    permission_classes = (AllowAnyPermission,)

class ApparelViewSet(viewsets.ModelViewSet):
    queryset = Apparel.objects.all()
    serializer_class = ApparelSerializer
    permission_classes = (AllowAnyPermission,)

class ApparelTagViewSet(viewsets.ModelViewSet):
    queryset = ApparelTag.objects.all()
    serializer_class = ApparelTagSerializer
    permission_classes = (AllowAnyPermission,)