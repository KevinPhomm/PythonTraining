import falcon


from wsgiref import simple_server

class DemoRessource:

    def on_get(self , req, resp):
        name = req.params.get("name", "nobody")
        resp.media = "coucou %s !" % name


#create web server
application = falcon.API()

#add api routes
application.add_route('/demo', DemoRessource())

#main for debug only
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()