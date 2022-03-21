from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('club', ClubViewSet, basename='club')
router.register('member', ClubMembersViewSet, basename='member')

urlpatterns = [
    # ViewSets:
    path('ViewSet/', include(router.urls)),
    path('ViewSet/<int:pk>/', include(router.urls)),


    # path('clubs/', club_list),
    #
    # api views:
    # path('clubs/', ClubAPIView.as_view()),  # {} to add new val
    # path('club_members/', ClubMembersAPIView.as_view()),  # {} to add new val
    # path('club_details/<int:pk>', club_details),
    # path('club_details/<int:pk>', ClubDetails.as_view()),
    # path('club_members/<int:pk>', ClubMembersDetails.as_view()),
    #
    # # Generic Views:
    # path('generic/clubs/<int:pk>/', ClubGenericAPIView.as_view()),
    # path('generic/club_members/<int:pk>/', ClubMembersGenericAPIView.as_view()),


]
