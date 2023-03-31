from rest_framework.serializers import Serializer, FileField, ValidationError, ModelSerializer
from .models import RemarkablePlaces


class UploadRemarkablePlacesSerializer(Serializer):
    file_upload = FileField()

    def validate(self, data):
        if str(data['file_upload'])[-5:] != '.xlsx':
            raise ValidationError("Wrong file format")
        return data

    class Meta:
        fields = ['file_upload']


class RemarkablePlacesSerializer(ModelSerializer):
    class Meta:
        model = RemarkablePlaces
        fields = ['name', 'lon', 'lat', 'rating']

