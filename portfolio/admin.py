from portfolio.models import Project, Item
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Project', {'fields': ['project', 'order_key', 'media_type', 'title']}),
            ('Item Text', {'fields': ['text','text_es','text_ca'],'classes':['collapse']}),
            ('Image', {'fields':['image','embed_field'], 'classes':['collapse']}),
            ]

class ItemInline(admin.TabularInline):
    model = Item
    exclude = ['height', 'width']
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name',]}),
            (None, {'fields': ['title', 'subtitle']}),
            ('Slug and Dates', {'fields': ['slug','start_date','end_date'], 'classes': ['collapse',]}),
            ('Image Preview', {'fields':['snapshot',], 'classes':['collapse',]}),
            ('Project Text', {'fields': ['text','text_es','text_ca'],'classes': ['collapse',]}),
            ]
    inlines = [ItemInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Item, ItemAdmin)
