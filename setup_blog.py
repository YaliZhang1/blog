import os
import json
import sqlite3
import random

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
    try:
        import django
        django.setup()
    except ImportError as exe:
        raise BaseException(exe.msg)

    # from django.db import transaction
        
    from blog.models import User, Category, Post
    from django.conf import settings
    from django.contrib.auth.models import User

    # -------------------------------------------------------------
    # delete all data exist
    # sqlite_sequence just for SQLite
    # -------------------------------------------------------------
    if settings.DATABASES['default']['ENGINE'].index('sqlite3'):
        con= sqlite3.connect("./db.sqlite3")
        cursor = con.cursor()
        cursor.execute('DELETE FROM blog_categories')
        # cursor.execute('DELETE FROM blog_users')
        cursor.execute('DELETE FROM auth_user where is_superuser != 1')
        cursor.execute('DELETE FROM blog_posts')
        # cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_users"')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="auth_user"')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_categories"')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_posts"')
        con.commit()
        con.close()
    else:
        User.objects.all().delete()
        Category.objects.all().delete()
        Post.objects.all().delete()
    # -------------------------------------------------------------

    category_list = ['general','community','interviews','meta','security']

    userData = [
        ('Johan', 'Johan@gmail.com', '88888888'),
        ('Qiang', 'admin@gmail.com', '88888888'),
        ('Magdalena', 'Magdaleda@gmail.com','88888888'),
        ('Yali', 'Yali@gmail.com', '88888888'),
        ('Raul', 'Raul@gmail.com', '88888888')
    ]
    
    userList = []
    for item in userData:
        userList.append(User.objects.create_user(item[0],item[1],item[2]))

    key = 0
    for value in category_list:
        key = key + 1
        tmp = { 'name':value, 'sort': key }
        category = Category.objects.create(**tmp)
        
        with open("./data/"+value+".json",'r') as f:
            for post in json.load(f):
                post = Post(title=post['title'],
                            body=post['content'],
                            category=category,
                            author=userList[random.randint(0,4)],
                            status=1)
                post.save()

    print("populate was successful")

if __name__ == '__main__':
    main()