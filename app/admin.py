from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class BottlePropLevelSpecifInline(admin.TabularInline):
    model = BottlePropLevelSpecif
    extra = 6
    max_num = 6


class BottleTaglSpecifInline(admin.TabularInline):
    model = BottleTagSpecif
    extra = 3


class BottleNewsSpecifInline(admin.TabularInline):
    model = NewsBottleSpecif
    extra = 3


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhotoSpecif
    extra = 3


class BottleAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [BottlePropLevelSpecifInline,BottleTaglSpecifInline]
    list_display = ('name', 'group')
    ordering = ('group',)
    list_filter = (
        ('group', admin.RelatedOnlyFieldListFilter),
    )


class NewsAdmin(SummernoteModelAdmin):
    inlines = [BottleNewsSpecifInline,NewsPhotoInline]

admin.site.register(News,NewsAdmin)
admin.site.register(NewsCategory)
admin.site.register(BottleProperties)
admin.site.register(Bottle,BottleAdmin)
admin.site.register(Wineglasses)
admin.site.register(FilterTag)
admin.site.register(BeerGroup,SummernoteModelAdmin)