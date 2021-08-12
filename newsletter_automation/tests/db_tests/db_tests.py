""" add unit tests to verify table structures , number of tables and pre-defined article categories"""

import unittest
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from newsletter.models import Articles, Article_category, AddNewsletter, NewsletterContent, Newsletter_schedule, Newsletter_campaign
from newsletter import db, app
from sqlalchemy import select,inspect,create_engine
from sqlalchemy import INTEGER,FLOAT,VARCHAR

class TestDatabase(unittest.TestCase):
    """ database integration tests """
    
    def setUp(self):
        """set the expected data required to validate the working db"""
        self.test_db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_TEST_URI'])
        self.test_inspector = inspect(self.test_db_engine)  
        self.db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        self.inspector = inspect(self.db_engine)
        self.all_tables_expected = sorted(['add_newsletter', 'article_category', 'articles', 'newsletter_campaign', 'newsletter_content', 'newsletter_schedule'])
        self.article_categories_expected = ['comic', 'pastweek', 'currentweek', 'automation corner']
    
    def test_database_contains_all_tables(self):
        """check test_db has all the expected tables"""
        self.assertEqual(self.all_tables_expected,self.inspector.get_table_names())
     
    def test_article_categories(self):
        """ validate pre-defined article categories in the db """
        self.assertEqual(self.article_categories_expected,[ctg[0] for ctg in db.session.query(Article_category.category_name).all()])
       
    def test_articles_schema(self):
        """verify articles table schema is as expected"""
        #self.maxDiff=None
        self.assertEqual(str(self.test_inspector.get_columns('test_articles')),str(self.inspector.get_columns('articles')))
        
    def test_add_newsletter_schema(self):
        """verify newsletter table schema is as expected"""
        self.assertEqual(str(self.test_inspector.get_columns('test_add_newsletter')),str(self.inspector.get_columns('add_newsletter')))
 
    def test_article_category_schema(self):
        """verify article_category table schema is as expected"""
        self.assertEqual(str(self.test_inspector.get_columns('test_article_category')),str(self.inspector.get_columns('article_category')))

    def test_newsletter_campaign_schema(self):
        """verify newsletter_campaign table schema is as expected"""
        self.assertEqual(str(self.test_inspector.get_columns('test_newsletter_campaign')),str(self.inspector.get_columns('newsletter_campaign')))

    def test_newsletter_content_schema(self):
        """verify newsletter_content table schema is as expected"""
        self.assertEqual(str(self.test_inspector.get_columns('test_newsletter_content')),str(self.inspector.get_columns('newsletter_content')))

    def test_newsletter_schedule_schema(self):
        """verify newsletter_schedule table schema is as expected"""
        self.assertEqual(str(self.test_inspector.get_columns('test_newsletter_schedule')),str(self.inspector.get_columns('newsletter_schedule')))


if __name__=='__main__':
    unittest.main(verbosity=2)

