import urllib.request 
from urllib.error import URLError,HTTPError,ContentTooShortError
import re

def download(url,user_agent='handy',num_tries=2,charset='utf-8'):
	print('Downlaoding:',url)
	request=urllib.request.Request(url)
	request.add_header('USer-agent',user_agent)
	try:
		# html = urllib.request.urlopen(url).read()
		# 1.CSS选择器
		resp=urllib.request.urlopen(request)
		cs= resp.headers.get_content_charset()
		if not cs:
			cs=charset
		html=resp.read().decode(cs)
	except(URLError,HTTPError,ContentTooShortError) as e:
		print('Download error:',e.reason)
		html=None
		if num_tries>0:
			if  hasattr(e,'code') and 500 <=e.code <600:
				# recursively retry 5xx Http erroes
				return download(url.num_tries -1)
	return html

def crawl_sitemap(url):
	# download the sitemap file
	sitemap=download(url)
	#extract the sitemap links
	links= re.findall('<loc>(.*?)</loc>',sitemap)
	#download each link
	for link in links:
		html=download(link)
		# -----


download('http://meetup.com')
crawl_sitemap('http://example.python-scraping.com/sitemap.xml')