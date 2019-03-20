from abc import ABC

import tornado.ioloop
import tornado.web


class PublicRentHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("rent.html", title="公共租赁房屋发布")


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("index.html", title="瑞祥爬虫系统")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
        (r"/rent", PublicRentHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
