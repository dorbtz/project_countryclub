from django.http import HttpResponse, JsonResponse
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.

# Generic ViewSet
class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubMembersViewSet(viewsets.ModelViewSet):
    serializer_class = ClubMembersSerializer
    queryset = ClubMembers.objects.all()


class ClubEventsViewSet(viewsets.ModelViewSet):
    serializer_class = ClubEventsSerializer
    queryset = ClubEvents.objects.all()

# generic based view
# class ClubGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.RetrieveModelMixin,
#                          mixins.DestroyModelMixin):
#     serializer_class = ClubSerializer
#     queryset = Club.objects.all()
#
#     lookup_field = 'pk'
#
#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self, request, pk=None):
#         return self.create(request, pk)
#
#     def put(self, request, pk=None):
#         return self.update(request, pk)
#
#     def delete(self, request, pk=None):
#         return self.destroy(request, pk)
#
#
# # generic based view (all actions in one page/location)
# class ClubMembersGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                                 mixins.UpdateModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 mixins.DestroyModelMixin):
#     serializer_class = ClubMembersSerializer
#     queryset = ClubMembers.objects.all()
#     lookup_field = 'pk'
#
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self, request, pk=None):
#         return self.create(request, pk)
#
#     def put(self, request, pk=None):
#         return self.update(request, pk)
#
#     def delete(self, request, pk=None):
#         return self.destroy(request, pk)
#
#
# # regular api view (need to post with {} to add new value)
# class ClubAPIView(APIView):
#
#     def get(self, request):
#         clubs = Club.objects.all()
#         serializer = ClubSerializer(clubs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ClubSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # regular api view (need to post with {} to add new value)
# class ClubMembersAPIView(APIView):
#
#     def get(self, request):
#         club_members = ClubMembers.objects.all()
#         serializer = ClubMembersSerializer(club_members, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ClubMembersSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ClubDetails(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Club.objects.get(pk=pk)
#
#         except Club.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         club = self.get_object(pk)
#         serializer = ClubSerializer(club)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         club = self.get_object(pk)
#         serializer = ClubSerializer(club, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         club = self.get_object(pk)
#         club.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class ClubMembersDetails(APIView):
#
#     def get_object(self, pk):
#         try:
#             return ClubMembers.objects.get(pk=pk)
#
#         except ClubMembers.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         club_member = self.get_object(pk)
#         serializer = ClubMembersSerializer(club_member)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         club_member = self.get_object(pk)
#         serializer = ClubMembersSerializer(club_member, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         club_member = self.get_object(pk)
#         club_member.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# function based api view
# @api_view(['GET', 'POST'])
# def club_list(request):
#     if request.method == 'GET':
#         clubs = Club.objects.all()
#         serializer = ClubSerializer(clubs, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ClubSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def club_details(request, pk):
#     try:
#         club = Club.objects.get(pk=pk)
#
#     except Club.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ClubSerializer(club)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ClubSerializer(club, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         club.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
