#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from django.utils import simplejson as json

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import logging

class Pygmentizer(webapp.RequestHandler):
    def post(self):
        #get language 
        lang = self.request.get('lang')
        #get code
        code = self.request.get('code')

        #format code
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        formatter.get_style_defs('.syntax')
        
        response = {"html": highlight(code, lexer, formatter)}
        
        #render json response
        self.response.out.write(json.dumps(response))


def main():
    application = webapp.WSGIApplication([('/pygmentize', Pygmentizer)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
