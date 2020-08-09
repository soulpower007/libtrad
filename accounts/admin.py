from django.contrib import admin
from .models import User, Book, Trade

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Trade)
