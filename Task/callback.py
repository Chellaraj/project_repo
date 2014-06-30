import tornado.ioloop
import tornado.web
import re
import os
import urllib
from Task1.tasks import getting_data_from_mysql
from tornado.web import StaticFileHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	table_name = repr(self.request.uri )
    	print table_name [ 8 : -1]
        result = getting_data_from_mysql( table_name [ 8 : -1] )
        if result == 1:
           self.write("%s data stored in csv file" % table_name [ 8 : -1] )
        else:
           self.write( result )

if __name__ == "__main__":
    #application.listen(8888)
    application = tornado.web.Application( [(r"/table/[\w\.-]+",MainHandler), ( r"/table/csv/(.*)",tornado.web.StaticFileHandler,{"path":"/home/linux/Task"}), ] )
    application.listen(8888)
    print application
    tornado.ioloop.IOLoop.instance().start()
