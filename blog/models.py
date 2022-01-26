from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICE = (
    (0, 'draft'),
    (1, 'published'),
    (2, 'deleted'),
)

# ----------------------------------------------------
class Category(models.Model):
    """
    Cateogry for Post
    """
    name = models.CharField(verbose_name="Name",
                            unique=True,
                            max_length=50,
                            blank=False,
                            null=False)
    sort = models.IntegerField(verbose_name="sort", default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "blog_categories"


# ----------------------------------------------------
class Post(models.Model):
    """
    POST
    """
    title = models.CharField(verbose_name="Title",
                             max_length=100,
                             blank=False,
                             null=False)
    
    visit = models.PositiveIntegerField(default=0,verbose_name="Visit")
    body = models.TextField(verbose_name="Content")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.SmallIntegerField(verbose_name="Status",
                                      choices=STATUS_CHOICE)

    created_at = models.DateTimeField(verbose_name="Created Time",
                                      auto_now_add=True,
                                      editable=False)
                                      
    updated_at = models.DateTimeField(verbose_name="Updated Time",
                                      auto_now=True,
                                      editable=False)

    def __str__(self) -> str:
        return self.title

    def getStatus(self):
        return STATUS_CHOICE[self.status][1]

    def visited(self):
        self.visit += 1
        self.save(update_fields=['visit'])

    class Meta:
        db_table = "blog_posts"
