import tornado.web

class route(object):
    """
    Example
    -------
    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass
    @route('/some/path', name='other')
    class SomeOtherRequestHandler(RequestHandler):
        pass
    my_routes = route.get_routes()
    """
    _routes = []

    def __init__(self, uri, name=None):
        self._uri = uri
        self.name = name

    def __call__(self, _handler):
        name = self.name and self.name or _handler.__name__
        self._routes.append(tornado.web.url(self._uri, _handler, name=name))
        return _handler

    @classmethod
    def get_routes(self):
        return self._routes
