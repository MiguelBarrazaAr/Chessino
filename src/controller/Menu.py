# -*- encoding: utf-8 -*-
from .Controller import Controller
from .MenuCtrl import *

class Menu(Controller):
    def start(self):
        self.options = [Config(self.engine),
            Increment(self.engine)]
        self.id=0
        self.play("menu")
        self.wait(0.5)
        self.callback(self.readMenu)

    def b1(self):
        self.mover(-1)

    def mover(self, x):
        self.eventClear()
        self.move(x)
        self.play("move")
        self.wait(0.1)
        self.callback(self.readMenu)

    def b2(self):
        print("lee negras")

    def w1(self):
        self.mover(1)

    def w2(self):
        print("lee blancas")

    def menu(self):
        self.play("exit")
        self.setController("Clock")

    def move(self, x):
        self.id = (self.id+x)%len(self.options)
    
    def getOption(self):
        return self.options[self.id]

    def readMenu(self):
        self.getOption().read()
