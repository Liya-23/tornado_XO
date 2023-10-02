import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\index.html", play = "", turns="", player_selected=False)   #, turns=""
    
    def post(self):
        start_player = self.get_argument("first_play")
        player = start_player
        player_selected = True

        self.render("web/index.html", play=player, turns= "its "+ player + "'s turn", player_selected=player_selected)



def make_app():
    return tornado.web.Application([ 
        (r"/", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"})
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9876)
    print("somethin on port 9876")
    tornado.ioloop.IOLoop.current().start()