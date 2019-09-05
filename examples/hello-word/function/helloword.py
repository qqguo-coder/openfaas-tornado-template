
import tornado.web
import tornado.gen

from common.routehelper import route


@route('/helloword')
class HelloWordHandler(tornado.web.RequestHandler):
    async def get(self):
        result = await self.doing()
        self.write(result)

    async def doing(self):
        await tornado.gen.sleep(2)
        return 'helloword'
