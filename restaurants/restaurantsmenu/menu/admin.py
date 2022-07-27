from django.contrib import admin
from .models import Section,Item,Modifiers


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']

admin.site.register(Section,SectionAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','section','name','description','price']

admin.site.register(Item,ItemAdmin)


# class ModifiersAdmin(admin.ModelAdmin):
#     list_display = ('id','name','description','price')
#
# admin.site.register(Modifiers,ModifiersAdmin)