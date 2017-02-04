#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnav Dhamija'
SITENAME = u'One in 7 Billion'
SITEURL = 'https://shortstheory.github.io'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

THEME = "pure-single"
TAGLINE = "Arnav's Blog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
PLUGINS = ['better_figures_and_images']
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
