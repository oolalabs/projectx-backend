from django.conf.urls import url, include
from rest_framework import routers

import projectx.views

# Router for autamatically handling route parsing
router = routers.DefaultRouter()
router.register(r'main_users', projectx.views.MainUserViewSet, base_name='main_users')

urlpatterns = [

	url(r'^api-v1/', include(router.urls)),

	# Landing Page
	url(r'^', projectx.views.index, name='index')

]