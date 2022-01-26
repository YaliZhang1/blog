from django.contrib import admin

from blog.models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort')

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'real_name', 'gender', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'status','created_at','updated_at','visit')