#coding=utf-8
import unittest
import urllib2

from bs4 import BeautifulSoup

from scraper import Scraper


class TestScraping(unittest.TestCase):
	"""
	some initials test for first preview of the class Scraper
	"""

	def setUp(self):
		self.word = 'hola'
		self.headers = {'User-Agent': 'Mozilla/5.0'}
		self.base_url = 'http://www.wordreference.com/definicion/' + self.word		

	def mk_response(self, url=None, read=True):
		if not url:
			url = self.base_url
		request = urllib2.Request(url, headers=self.headers)
		response = urllib2.urlopen(request)
		if read:
			return response.read()
		return response

	def get_input_hidden(self):
		response = self.mk_response()
		soup = BeautifulSoup(response)
		return soup.find('input', id='aud')


	def test_request_url(self):		
		response = self.mk_response()
		self.assertTrue(self.word in response)

	def test_exists_hidden_field(self):
		self.assertIsNotNone(self.get_input_hidden())

	def test_exists_url_sound(self):
		url = 'http://www.wordreference.com/audio/es/es/ogg/%s-11.ogg' % self.get_input_hidden().get('value')
		response = self.mk_response(url=url, read=False)
		self.assertTrue(response.code == 200)

	def test_scraper_class_works_fine(self):
		"""
		finally check the class Scraper works fine:
		"""
		scraper = Scraper('hola')
		self.assertIn('ogg', scraper.get_url_sound())


if __name__ == '__main__':
	unittest.main()
