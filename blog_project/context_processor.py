from django.contrib.auth.models import User
from blog.models import Category

def pasteCategory(request):
    # TODO need to set up a white list
    category_list = Category.objects.order_by('sort')
    return {'category_list':category_list}

def pasteUser(request):
    # TODO need to set up a white list
    user_list = User.objects.filter(is_superuser=False).order_by('username')
    return {'user_list':user_list}