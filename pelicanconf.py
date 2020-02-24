#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

SITENAME = 'The Atari and Retro Site of Goz'

TIMEZONE = 'America/New_York'

MARKUP = (('rst', 'md', 'markdown'))

AUTHOR = 'gozar'
DEFAULT_DATE = 'fs'
THEME = 'pelican-attila'

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_ATOM = None

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

AUTHOR_URL = ('author/{slug}/')  
AUTHOR_SAVE_AS = ('author/{slug}/index.html')

CATEGORY_URL = ('category/{slug}/') 
CATEGORY_SAVE_AS = ('category/{slug}/index.html')  
TAG_URL = ('tag/{slug}/') 
TAG_SAVE_AS = ('tag/{slug}/index.html')

PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}/index.html')

#FEED_RSS = 'feed/index.html'
#FEED_ALL_RSS = 'feed/index.rss'
#CATEGORY_FEED_RSS = 'feed/category/{slug}.rss'
#TAG_FEED_RSS = 'feed/tag/{slug}.rss'

DELETE_OUTPUT_DIRECTORY = True

# Pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

STATIC_PATHS = ['extra/CNAME','images',]
EXTRA_PATH_METADATA = {
            'extra/CNAME': {'path': 'CNAME'},
                }

LINKS = (
            ('RSS', "feeds/all.atom.xml")
            )

AUTHORS_BIO = {
        "gozar": {
            "name":"Ryan 'Gozar' Collins",
            "website": "https://ryancollins.org",
            "image": "https://gtia.com/images/gozavatar.png",
            "location": "Earth",
            "bio": "What, me worry?"
            }
        }

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
THEME = 'themes/attila'

MENUITEMS = (
    ('About', '/about/'),
    ('Hardware', '/category/hardware/'),
    ('Software', '/category/software/')
    )

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme settings
HEADER_COVER = '/images/Atari800-header.jpg'
