from django.contrib import admin
from .models import Rack, Book, RackItem
# Register your models here.

admin.site.register(Book)
admin.site.register(Rack)
admin.site.register(RackItem)
