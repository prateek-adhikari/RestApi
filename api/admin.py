from django.contrib import admin
from api.models import Article,Tag
# Register your models here.

admin.site.register([
    Article,
    Tag,
])