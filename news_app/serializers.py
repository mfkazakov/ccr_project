from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ImageField

from .models import News


class NewsSerializer(ModelSerializer):
    image_thumb = ImageField(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'publication_date', 'author', 'image', 'image', 'image_thumb']

