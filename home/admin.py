from django.contrib import admin
from .models import Books, Readers, Borrowed_books
# Register your models here.


admin.site.register(Books)
admin.site.register(Readers)
admin.site.register(Borrowed_books)
