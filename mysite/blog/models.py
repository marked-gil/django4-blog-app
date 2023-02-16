from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """
    Custom manager to retrieve posts with PUBLISHED status
    """
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        """
        An enumration class by subclassing models.TextChoices.
        choices are: DRAFT, PUBLISHED.
        values are: DF & PB.
        labels (readable names) are: Draft & Published.
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # CharField translates into VARCHAR column in SQL database
    title = models.CharField(max_length=250)
    # SlugField translates into VARCHAR column in SQL database
    # slug is a short label that contains only letters, numbers, underscores, and hyphens
    slug = models.SlugField(max_length=250)
    # Defines a many-to-one relationship between Post and User
    # Django will create a foreign key in the database using PK of User
    # related_name - name of the reverse relationship, from User to Post (eg, user.blog_posts)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    # TextField translates into TEXT column in SQL database
    body = models.TextField()
    # DateTimeField translates into DATETIME column in SQL database
    # timezone.now returns the current datetime in a timezone-aware format
    publish = models.DateTimeField(default=timezone.now)
    # auto_now_add automatically adds/saves the current datetime to the database
    created = models.DateTimeField(auto_now_add=True)
    # auto_now updates date automatically when saving an object
    updated = models.DateTimeField(auto_now=True)
    # Limits the value of the field with choices parameter
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager() # default manager
    published = PublishedManager() # our custom manager
    
    class Meta:
        # specifies the ordering of posts in descending order (hyphen before field name)
        ordering = ['-publish']
        # Adds an index for the publish field in descending order;
        # This will improve performance for queries filtering or ordering results by this field.
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """
        Returns a string with human-readable representation of the object.
        Django will use this method to display the name of the object in many places.
        """
        return self.title
