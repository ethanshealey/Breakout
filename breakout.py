from vpython import *

def game():

    class block():
        def __init__(self, x, y):
            self.b = box(pos=vector(-7.1+(x*1.1),4-y,0),
                        color=color.yellow,
                        size=.2*vec(5,2,1))

        def collide(self, s):
            if (s.pos.x >= self.b.pos.x - .5) and (s.pos.x <= self.b.pos.x + .5) and (s.pos.y <= self.b.pos.y + .4 and s.pos.y >= self.b.pos.y - .4):
                self.b.pos = vec(-10000, -10000, 0)
                return True

    scene = canvas(title="<b>Blockbuster!</b><br>Note: This was created in 30 minutes")
    scene.range = 5
    pad = box(pos=vector(0,-4,0),
            color=color.cyan,
            size=0.2*vec(10,1,1))

    s = sphere(pos=vector(0,-2,0),
            color=color.red,
            size=.3*vec(1,1,1))

    s.v = vector(-.025,-.075,0)

    blocks = []
    y = 0
    for y in range(0, 5):
        for x in range(0, 14):
            blocks.append(block(x, y))

    scene.pause("Click to play!")

    while True:
        if scene.mouse.pos.x > -7 and scene.mouse.pos.x < 7:
            pad.pos.x = scene.mouse.pos.x
        elif scene.mouse.pos.x < -7:
            pad.pos.x = -7
        elif scene.mouse.pos.x > 7:
            pad.pos.x = 7
        s.pos = s.pos + s.v * .006

        # Collides with Pad
        if (s.pos.x >= pad.pos.x - 1 and s.pos.x <= pad.pos.x + 1) and (s.pos.y <= pad.pos.y + .2 and s.pos.y >= pad.pos.y - .2):
            s.v.y = -s.v.y

        # Collides with Floor
        if s.pos.y < -5:
            scene.pause("Game Over!\nClick to play again!")
            scene.title = ""
            scene.delete()
            game()

        # Collides with wall
        if s.pos.x < -7.9 or s.pos.x > 7.9:
            s.v.x = -s.v.x

        # Collides with roof
        if s.pos.y > 4.8:
            s.v.y = -s.v.y

        # Collides with a block
        for block in blocks:
            if block.collide(s) == 1:
                s.v.y = -s.v.y

game()