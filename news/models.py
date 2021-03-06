from distutils.command.build_scripts import first_line_re
import email
import datetime as dt
from email.policy import default

from django.db import models

# Create your models here.
class Editor (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank = True)

    def __str__(self):
        return self.first_name
    # meta class that specifies default ordering specific to this model class
    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save(self)
    def delete_editor(self):
        
        self.delete(self)

    def update_editor(self):
        self.update(self)
        


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete= models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    artcle_image = models.ImageField(upload_to = 'articles/',default="")

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


     