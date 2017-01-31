#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnav Dhamija'
SITENAME = u'One in 7 Billion'
SITEURL = 'https://shortstheory.github.io'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

THEME = "pure-single"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PATH = 'content'

COVER_IMG_URL = 'images/StarStaX_IMG_9937-IMG_9966_lighten.jpg'
PROFILE_IMG_URL = 'images/profile.jpg'

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
          ("youtube", "https://www.youtube.com/channel/UCzOTlzNDylDXSBxKSJlBzuQ"),
          ("instagram", "https://www.instagram.com/arnavdhamija"),
#          ("linkedin", "https://www.linkedin.com/in/arnav-dhamija-b98160129"),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
