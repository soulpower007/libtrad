from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from django.db import models


class User(AbstractUser):
    slug = models.CharField(blank=True, max_length=75)
    is_librarian = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    whatsappno = models.CharField(blank = True,null=True, unique=True, max_length=15)

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="book_images/")
    membership_req = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    owner = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE, related_name='owned_books')
    keeper = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE, related_name='kept_books')

    def __str__(self):
        return self.name

class Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    requestor = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE, related_name='requested_books')
    book = models.ForeignKey(Book,blank=True, null=True, on_delete=models.CASCADE, related_name='book_reqs')
    approver = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE, related_name='authorize_books')
    did_approve = models.BooleanField(default = False)
    did_view = models.BooleanField(default = False)

    @classmethod
    def create(cls, requestor, book, approver):
        trade = cls(requestor =requestor, book=book, approver=approver)
        return trade

    def __str__(self):
        return self.requestor.username + " for " + self.book.name + " " + self.approver.username
