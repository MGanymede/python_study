import os
from abc import ABC

import tornado.ioloop
import tornado.web
from Tornado_study.fetcher.Rent import Rent

rent = Rent()


class PublicRentHandler(tornado.web.RequestHandler, ABC):

    def get(self):
        rent_data = rent.get_rent_data()
        self.render("rent.html", title="公共租赁房屋发布", data=rent_data,
                    refreshDate=rent.fetchDate)


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("index.html", title="瑞祥爬虫系统")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/rent", PublicRentHandler)
    ], static_path=os.path.join(os.path.dirname(__file__), "static"))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
