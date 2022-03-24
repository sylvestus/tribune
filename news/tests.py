from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        # editor
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

         # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        # article
        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # tesing save method
    def test_save_method(self):
        # self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
    # tesing delete method
    def test_delete_method(self):
        
        self.james.delete_editor()
        editors= Editor.objects.all()
        self.assertTrue(len(editors)<1)
        
    def test_update_method(self):
        # self.james.save_editor()
        self.james.update_editor()
        editors = Editor.objects.filter(id = 1).update(first_name ='Kim')

        self.assertTrue(editors.first_name!= 'james')

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    




