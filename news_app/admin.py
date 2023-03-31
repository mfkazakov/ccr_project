from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News
from django.utils.safestring import mark_safe


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    """Админка для новостей"""
    list_display = ('title', 'publication_date', 'author')
    readonly_fields = ('get_image',)
    summernote_fields = ('text', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_thumb.url} width=auto height=auto')

    get_image.short_description = "Изображение"

