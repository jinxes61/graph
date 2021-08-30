from test_input import TextInput

class Settings:

    def __init__(self):
        #sets of screen
        self.screen_size = (1080, 720)
        self.bg_color = (255, 255, 255)

        #sets of status
        self.status = 0

        #sets of stars
        self.star_num = 7
        self.star_speed = 1
        self.star_build = 0
        self.star_mov = 0

        #sets of button
        self.button_pos = (480, 450, 120, 50)

        #sets of graph
        self.node_num = 4
        self.node_r = 20
        self.graph_bg = (520, 130, 520, 520)
        self.node_moving = 10
        self.nodes_edges = []

        #sets of add or del nodes
        self.add_or_del = 0
        self.txt = TextInput()
        self.invalid = False