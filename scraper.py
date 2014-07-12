#coding=utf-8
import urllib2

from bs4 import BeautifulSoup


class Scraper(object):

	def __init__(self, word=None):
		self.word = word

	def __mk_reponse(self, url, read=True):
		headers = {'User-Agent': 'Mozilla/5.0'}
		request = urllib2.Request(url, headers=headers)
		response = urllib2.urlopen(request)
		if read:
			return response.read()
		return response

	def __exists_sound(self):
		url = 'http://www.wordreference.com/definicion/' + self.word
		response = self.__mk_reponse(url)
		soup = BeautifulSoup(response)
		a_href = soup.find('a', id='audspeaker')
		if a_href:
			input_hidden = soup.find('input', id='aud')
			if input_hidden:
				return input_hidden.get('value')
		return None

	def get_url_sound(self, word=None):
		if word:
			self.word = u''.join(word).encode('utf-8')
		id_sound = self.__exists_sound()
		if id_sound:
			url_sound = 'http://www.wordreference.com/audio/es/es/ogg/%s-11.ogg' % id_sound
			response = self.__mk_reponse(url_sound, read=False)
			if response.code == 200:
				return url_sound
		return None
