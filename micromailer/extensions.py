# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_marrowmailer import Mailer

cache = Cache()
debug_toolbar = DebugToolbarExtension()
mailer = Mailer()
