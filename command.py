'''
    Command pattern
    - A method call wrapped in an object.
    - synonyms in other languages: “callback, “first-class function”, “function pointer”, “closure”, or “partially applied function” 
'''

class GameActor:
    '''
    Character class in game world
    '''
    def jump(self):
        print('Jump')

class Command:
    def execute(self, actor):
        pass

class JumpCommand(Command):
    def execute(self, actor):
        actor.jump()

class InputHandler:
    BUTTON_X = 'X'
    BUTTON_Y = 'Y'
    BUTTON_A = 'A'
    BUTTON_B = 'B'

    def __init__(self, actions):
        self.button_x = actions['x_action']
        self.button_y = actions['y_action']
        self.button_a = actions['a_action']
        self.button_b = actions['b_action']

    def is_pressed(self, button):
        pass

    def handle_input(self):
        if self.is_pressed(self.BUTTON_X):
            return self.button_x
        elif self.is_pressed(self.BUTTON_Y):
            return self.button_y
        elif self.is_pressed(self.BUTTON_A):
            return self.button_a
        elif self.is_pressed(self.BUTTON_B):
            return self.button_b
        return None

input_handler = InputHandler({
    'x_action': JumpCommand,
    'y_action': JumpCommand,
    'a_action': JumpCommand,
    'b_action': JumpCommand,
})

command = input_handler.handle_input()
player = GameActor()
if command:
    command().execute(player)