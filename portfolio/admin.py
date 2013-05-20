from portfolio.models import Project, Item, Download
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Project', {'fields': ['project', 'order_key', 'media_type', 'title']}),
            ('Item Text', {'fields': ['text',],'classes':['collapse']}),
            ('Image', {'fields':['image',], 'classes':['collapse']}),
            ]

class ItemInline(admin.TabularInline):
    model = Item
    exclude = ['height', 'width']
    extra = 1
    fields = (
            'order_key',
            'image',
            'title',
            'text',
            )

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name',]}),
            (None, {'fields': ['title', 'subtitle']}),
            (None, {'fields': ['slug','snapshot','text'],}),
            ]
    inlines = [ItemInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Download)
