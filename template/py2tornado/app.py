import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define, options

from common.routehelper import route
try:
    import function
except ImportError:
    raise ("Function Not Found.")

define("port", default=5000, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=route.get_routes())
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
