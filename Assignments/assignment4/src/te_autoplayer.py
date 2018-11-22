''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction

class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        self.random_next_move(gamestate)

                
    def search_all(self, gamestate):
        left = Direction.LEFT
        right = Direction.Right
        x = 1
        y = 1
        
        for i in range(16):
            clone = gamestate.clone(True)
                for j in range(x):
                    clone.move(left)
                    for k in range(y):
                        clone.rotate()
                        clone.update()
                        if y<4:
                            y+=1
                        else:
                            y=1
                            x+=1       
        
        
        
        
        
        
        
        ''' make a random move and a random rotation.  Not the best strategy! '''
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.move(direction)
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.rotate(direction)
        gamestate.print_block_tiles()
        
