# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Config(MenuItem):
    def start(self):
        self.engine.display('config tiempo')
        self.audio = "configurar-tiempos"

    def back(self):
        pass

    def next(self):
        pass
