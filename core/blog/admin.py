from django.contrib import admin
from .models import BlogPostModel,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
admin.site.register(BlogPostModel,BlogAdmin)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
admin.site.register(Category,CategoryAdmin)