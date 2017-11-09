# -*- coding: utf-8 -*-

from rest_framework import status
from django.http import JsonResponse


def index(request):
    return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)