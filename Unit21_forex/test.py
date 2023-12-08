from unittest import TestCase
from app import app
from forex import convert, currency_symbol

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ForexConvertTests(TestCase):
    """Test Foreign Converter App"""
    
    def test_convert(self):
        API = 'convert'
        KEY = '9fe18299682790786003cc50793e2111'
        self.assertEqual(convert(API,KEY,'aud','aud',1), 1)
        self.assertEqual(convert(API,KEY,'USD','USD',1), 1)
        self.assertEqual(convert(API,KEY,'usd','usd',1), 1)
        
    def test_currency_symbol(self):
        self.assertEqual(currency_symbol('nzd'),'NZ$')
        self.assertEqual(currency_symbol('SGD'),'S$')
    
    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<button id="add-message">Convert</button>', html)
            self.assertIn('<li>EUR: Euro</li>', html)
            
    def test_currency_submit(self):
        with app.test_client() as client:
            res = client.post('/form', data={'cfrom':'HKD','cto': 'HKD','amount':400})
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code,200)
            self.assertIn('<h1>The result is HK$ 400.</h1>',html)
            
            
    
    