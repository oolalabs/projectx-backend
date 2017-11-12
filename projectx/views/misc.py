# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.http import JsonResponse

from projectx.models import *
from projectx.serializers import *
from projectx.permissions import *



def index(request):
    return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (AllowAnyPermission,)