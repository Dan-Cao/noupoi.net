#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Noupoi'
SITENAME = 'Noupoi.net'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
    'extensions': ['mdx_include']
}

STATIC_PATHS = ['static']

# Theme settings
THEME = 'MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/pure-min.css'
# MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2020
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Noupoi\'s website'
# AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
# AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
# AUTHOR_WEB = 'http://mypersonalsite.com'

# Services
GOOGLE_ANALYTICS = 'UA-139603630-2'
# DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
    # ('facebook', 'http://www.facebook.com/johndoe'),
    # ('twitter', 'http://twitter.com/johndoe'),
    # ('github', 'https://github.com/johndoe'),
    # ('linkedin', 'http://www.linkedin.com/in/johndoe'),
)

# Menu
MENUITEMS = (
    # ('Categories', '/' + CATEGORIES_SAVE_AS),
    # ('Archive', '/' + ARCHIVES_SAVE_AS),
)
