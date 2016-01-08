#!/usr/bin/env python
"""
From:
    https://gist.github.com/tomalrussell/0828db8491b99db032fe

With minor cleanups, etc.

Usage:
    python jekyll-new-post.py "Title" category1 category2 etc.
"""
from __future__ import print_function
import sys
import datetime
import os

# set title to command-line argument, or default
if (len(sys.argv) > 1):
    title = sys.argv[1]
else:
    title = "New Post"

# use the rest of the arguments for categories
categories = " ".join(sys.argv[2:])

# standard filename format: date and title
filename = datetime.datetime.now().strftime('%Y-%m-%d-') + \
    title.lower().replace(" ", "-") + '.md'

# standard front matter: title, full date, categories
front_matter = '''\
---
layout: post
title: %s
date: %s
categories: %s
---
''' % (title, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), categories)

# if we're in a jekyll root, pop it in ./_posts
if(os.path.exists(os.getcwd() + '/_posts')):
    filepath = os.getcwd() + '/_posts/' + filename
else:
    filepath = os.getcwd() + '/' + filename

# check if this post exists already, otherwise create and write!
if(os.path.exists(filepath)):
    print ("Looks like this post already exists: " + filepath)
else:
    with open(filepath, 'w') as f:
        print(front_matter, file=f)
        print("Post created! " + filename)
