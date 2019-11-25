from django.contrib import admin

from sahibinden.models import Post
from sahibinden.models import Property
from sahibinden.models import Detail
from sahibinden.models import Picture

admin.site.register(Post)
admin.site.register(Property)
admin.site.register(Detail)
admin.site.register(Picture)
# Register your models here.
