from django.conf.urls import url, include
from rest_framework import routers

import projectx.views

# Router for autamatically handling route parsing
router = routers.DefaultRouter()
router.register(r'main_users', projectx.views.MainUserViewSet, base_name='main_users')
router.register(r'likes', projectx.views.LikeViewSet, base_name='likes')
router.register(r'comments', projectx.views.CommentViewSet, base_name='comments')
router.register(r'saves', projectx.views.SaveViewSet, base_name='saves')
router.register(r'apparel_types', projectx.views.ApparelTypeViewSet, base_name='apparel_types')
router.register(r'apparels', projectx.views.ApparelViewSet, base_name='apparels')
router.register(r'apparel_tags', projectx.views.ApparelTagViewSet, base_name='apparel_tags')
router.register(r'hashtags', projectx.views.HashTagViewSet, base_name='hashtags')
router.register(r'hashtag_links', projectx.views.HashTagLinkViewSet, base_name='hashtag_links')
router.register(r'locations', projectx.views.LocationViewSet, base_name='locations')
router.register(r'outfits', projectx.views.OutfitViewSet, base_name='outfits')
router.register(r'medias', projectx.views.MediaViewSet, base_name='medias')


urlpatterns = [

	# Authentication
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # API Endpoints
	url(r'^api-v1/', include(router.urls)),
	url(r'get_self', projectx.views.get_self),

	# Landing Page
	url(r'^', projectx.views.index, name='index')

]