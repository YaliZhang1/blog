import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog_project.settings')

import django
django.setup()

import random
from blog.models import User,Category,Post
from faker import Faker

fakegen = Faker()
#users = ['Yali','Johan','Magdalena','Raul','Qiang']
#def add_user():
#    name2=random.choice(users)
#    u = User.objects.get_or_create(name = name2)[0]
#    u.save()
#    return u

#categories = ['Search','Social','Marketplace','News','Games']
#def add_category():
#    name1=random.choice(categories)
#    t = Category.objects.get_or_create(name = name1)[0]
#    t.save()
#    return t


#def populate():
#    category = add_category()
#    author = add_user()
#    fake_title = fakegen.string()
#    fake_body = fakegen.body()
#    fake_status = fakegen.status()
#    fake_created_at = fakegen.date()
#    fake_updated_at = fakegen.date()
#    fake_sort=fakegen.sort()

#    fake_name1 = fakegen.name1()
#    fake_name2 = fakegen.name2()
#    fake_password = fakegen.password()
#    fake_real_name = fakegen.real_name()
#    fake_gender = fakegen.gender()
#    fake_email = fakegen.email()
    

#    Use = User.objects.get_or_create(name2=fake_name2,password=fake_password,real_name=fake_real_name,gender=fake_gender,email=fake_email)[0]
#    Cat = Category.objects.get_or_create(name1=fake_name1,sort=fake_sort)[0]
#    Po = Post.objects.get_or_create(title=fake_title,body=fake_body,status=fake_status,created_at=fake_created_at,updated_at=fake_updated_at,author = Use,category = Cat)[0]

users = ['Yali','Johan','Magdalena','Raul','Qiang']
def add_user():
    random_name = random.choice(users)
    fake_password = fakegen.password()
    fake_real_name = fakegen.name()
    random_gender = random.randint(0, 2)
    fake_email = fakegen.email()

    u, created = User.objects.get_or_create(name = random_name, defaults = {'real_name': fake_real_name, 
        'gender': random_gender, 'email': fake_email})
    if created:
        u.password(fake_password)
        u.save()
    return u
    

categories = ['Technology','Social','Love','News','Economy']
def add_category():
    random_name = random.choice(categories)
    random_sort = random.randint(0, 10000)
    c = Category.objects.get_or_create(name = random_name, defaults = {'sort': random_sort})[0]
    c.save()
    return c

def populate():
    new_category = add_category()
    new_author = add_user()
       
    fake_title = fakegen.text().split()[0]
    fake_body = fakegen.text() + " " + fakegen.text() + " " + fakegen.text() + " " + fakegen.text()
    random_status = random.randint(0, 2)
    fake_created_at = fakegen.date_time()
    fake_updated_at = fakegen.date_time()

    
    post = Post.objects.get_or_create(title = fake_title, body = fake_body,
        status = random_status, created_at = fake_created_at,
        updated_at = fake_updated_at, author = new_author, category = new_category)[0]

if __name__ == '__main__':
    print("populating script!")
    
    for _ in range(60):
       populate()

    #r = Post.objects.filter()
    #r._raw_delete(r.db)

    #s = Category.objects.filter()
    #s._raw_delete(s.db)

    print("populating complete!")

