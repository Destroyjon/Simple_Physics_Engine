import pygame
from Old_Code_Stuff.jsLib import constrain, Vector


class mover:
    def __init__(self, x=0, y=0, z=0, m=1, color=(0, 0, 0)):
        self.pos = Vector(x, y)
        self.vel = Vector.random2D()
        # self.vel.mult(random.uniform(0, 1))
        self.acc = Vector()
        self.mass = m
        self.r = (self.mass ** 0.5) * 20
        self.collider = Vector()
        self.color = color

    def setRadius(self, radius):
        self.r = radius

    def getRadius(self):
        radius = str(self.r)
        return radius

    def setColor(self, color):
        self.color = color

    def getColor(self):
        color = str(self.color)
        return color

    def applyforce(self, force: Vector):
        f = force/self.mass
        self.acc += f

    def friction(self, height):
        diff = height - (self.pos.y + self.r)
        if diff < 1:
            # print('friction')
            friction = self.vel
            friction = friction.normalize()
            friction *= -1

            mu = 0.001
            normal = self.mass
            friction = friction.setMag(mu * normal)
            self.applyforce(friction)

    def edges(self,width=700, height=700):
        if self.pos.y >= height-self.r:
            self.pos.y = height-self.r
            self.vel.y *= -0.5
        if self.pos.y <= 0+self.r:
            self.pos.y = 0+self.r
            self.vel.y *= -0.5

        if self.pos.x >= width-self.r:
            self.pos.x = width-self.r
            self.vel.x *= -0.5
        if self.pos.x <= 0+self.r:
            self.pos.x = 0+self.r
            self.vel.x *= -0.5

    def collision(self, colliders):
        collisionR = self.r + 10
        for i in colliders:
            if self.pos.y > i.collider.y and self.pos.y < i.collider.y + collisionR or self.pos.y + collisionR > i.collider.y and self.pos.y + collisionR < i.collider.y + collisionR:
                if self.pos.x > i.collider.x and self.pos.x < i.collider.x + collisionR or self.pos.x + collisionR > i.collider.x and self.pos.x + collisionR < i.collider.x + collisionR:
                    self.pos.y = ((self.pos.y) - (i.r/2))
                    self.pos.x = ((self.pos.x) - (i.r/2))
                    normVel = (self.vel-i.vel).normalize()
                    self.applyforce(normVel)

    def setMass(self, mass):
        self.mass = mass
        return self.mass


    def update(self):
        mouse = pygame.mouse.get_pos()
        mouse = Vector(mouse[0], mouse[1])
        # self.acc = Vector.subS(mouse, self.pos)
        # self.acc = self.acc.setMag(0.01)

        self.vel += self.acc
        # self.vel = self.vel.limit(4)
        self.pos = constrain(self.pos + self.vel, 0, 700)
        self.collider = self.pos
        self.acc = Vector()
        self.pos

    def show(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.r)
        # pygame.draw.rect(screen, (0, 0, 0), (self.pos.x-self.r, self.pos.y-self.r, self.r, self.r), 1, 1)
        # pygame.draw.line(screen, (0, 0, 0), (self.pos.x, self.pos.y), (self.pos.x+self.vel.x*30, self.pos.y+self.vel.y*30), 5)
