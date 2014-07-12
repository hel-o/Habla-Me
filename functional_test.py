#coding=utf-8
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestFunctional(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_check_user_input_word(self):
		self.browser.get('http://127.0.0.1:5000/')
		self.assertIn('Habla-Me', self.browser.title)

		input_word = self.browser.find_element_by_name('word')
		input_word.send_keys('hola')
		input_word.send_keys(Keys.ENTER)

		self.assertIn('ogg', self.browser.find_element_by_tag_name('h3').text)


if __name__ == '__main__':
	unittest.main()
