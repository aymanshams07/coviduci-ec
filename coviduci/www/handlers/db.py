import tornado.web
from coviduci.www.handlers import base
from coviduci.www.handlers import home


class DBHandler(base.BaseHandler):

  ROUTE = '/db/(.*)'

  def initialize(self, db):
    self.db = db
    keys = ['data']
    self.get_fns = {k: getattr(self.db, f'get_{k}', None) for k in keys}

  def get(self, collection):
    get_fn = self.get_fns.get(collection, None)
    if get_fn is not None:
      self.write(get_fn().to_html())
    else:
      self.redirect(home.HomeHandler.ROUTE)
