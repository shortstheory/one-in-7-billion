#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnav Dhamija'
SITENAME = u'A Singularity'
SITEURL = 'http://arnavdhamija.com'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

THEME = "pure-single"
TAGLINE = "Arnav Dhamija's Weblog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = SITEURL
FEED_ALL_ATOM = "feeds/atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"
TAG_FEED_RSS = "feeds/tag_%s.rss.xml"

GOOGLE_ANALYTICS = "UA-91464572-1"
DISQUS_SITENAME = "arnavdhamija"
DISQUS_PUBLIC_KEY = "gdd4lFggU04G6SXD6gaqbeN1Kzsid3ZTXsn4b023V0mC1EPxIWeWNRMbpTp92Nqe"
DISQUS_PRIVATE_KEY = "3MnB3GHMR1q4q83MLN86sW1YJmY4ozyMIaULmKPyAVYUMH9etNzeBvtvvEVZBldv"
GITHUB_URL = "https://github.com/shortstheory"

PATH = 'content'
STATIC_PATHS = ['images']

ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
INDEX_SAVE_AS = 'index.html'
#INDEX_URL = 'blog/'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAGS_URL = 'blog/tag/'
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

COVER_IMG_URL = '/images/StarStaX_IMG_9937-IMG_9966_lighten.jpg'
PROFILE_IMG_URL = '/images/profile.jpg'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['disqus_static', 'photos']

PHOTO_LIBRARY = "content/images"
PHOTO_ARTICLE = (760, 506, 80)

RESPONSIVE_IMAGES = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (("github", "https://github.com/shortstheory"),
          ("youtube", "https://www.youtube.com/user/shortstheory"),
          ("instagram", "https://www.instagram.com/arnavdhamija"),
#          ("linkedin", "https://www.linkedin.com/in/arnav-dhamija-b98160129"),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
