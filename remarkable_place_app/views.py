from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from .selializers import UploadRemarkablePlacesSerializer, RemarkablePlacesSerializer
from rest_framework.response import Response
from .services.extract_data_from_file import RemarkablePlacesFromFile


class UploadRemarkablePlacesViewSet(CreateModelMixin, viewsets.ViewSet):
    serializer_class = UploadRemarkablePlacesSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        file_uploaded = request.FILES.get('file_upload')

        serializer = RemarkablePlacesSerializer(data=RemarkablePlacesFromFile(file_uploaded).get_items(), many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

