import os
import random
import cherrypy

class Battlesnake(object):

    def __init__(self):
        # board height and width
        self.board_height = 0
        self.board_width = 0


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):        
        
        return {
            "apiversion": "1",
            "author": "withrvr",
            "color": "#6441a5", # twitch color code
            "head": "silly",
            "tail": "skinny",
        }


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):

        # setting the size
        self.board_height = data["board"]["height"] - 1
        self.board_width  = data["board"]["width"]  - 1
        self.terminate_turn = (2 * (self.board_height + self.board_width))

        print()
        print(board_height)
        print(board_width)
        print(terminate_turn)
        print()

        print("\nSTART\n")
        return "ok"


    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        """
        self current code
        just move snake
        anti-click-wise from the edges

        more advance in development

        """

        data = cherrypy.request.json

        # default move of the snake
        move = 'left'

        # head x and y value of snake
        head_x = data["you"]["head"]["x"]
        head_y = data["you"]["head"]["y"]

        
        # checking the corner of the board

        # bottom-left corner
        if head_x == 0 and head_y == 0:
            move = 'right'
        # bottom-right corner
        elif head_x == 0 and head_y == self.board_width:
            move = 'up'
        # top-right corner
        elif head_x == self.board_height and head_y == self.board_width:
            move = 'left'
        # top-left corner
        elif head_x == 0 and head_y == self.board_width:
            move = 'down'


        # foo-foo-foo code to terminate the process

        # if data["turn"] > self.terminate_turn:
        #     move = ''

        print(f"\nMOVE: {move}\n")
        return {"move": move}


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        
        print("\nEND\n")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("\nStarting Battlesnake Server...\n")
    cherrypy.quickstart(server)
