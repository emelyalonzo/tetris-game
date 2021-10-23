import random

class Figure ():
    #Figures of the game
    figures = [
        [[1,5,9,13],[4,5,6,7]],
        [[1,2,5,9],[0,4,5,6],[1,5,8,9],[4,5,6,10]],
        [[1,2,6,10],[5,6,7,9],[2,6,10,11],[3,5,6,7]],
        [[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,9]],
        [[1,2,4,5],[0,4,5,9]],
        [[0,1,5,6],[2,5,6,9]],
        [1,2,5,6]
    ]

    def __init__ (self, x,y):
        self.x = x,
        self.y = y,
        self.type = random.randint(0, len(self.figures))
        self.color = random.randint(1, len(colors)) #It is required to define a colors array depending on the Pygame interface
        self.rotation = 0

    def image(self):
        #Select the image in the matrix "figures" (self.type x self.rotation)
        return self.figures[self.type][self.rotation]

    def rotate(self):
        #Choses the next rotation of the figure, without getting off the possible rotations.
        """For example, if you are in the figure 0 and there are 4 rotations, if rotate is called then
        it will end in 1%4 = 1, but if you are in the figure 3 and rotate is called then 4%4=0 which will lead you
        to the first figure 0 again."""
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
    