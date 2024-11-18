class Control:
    def __init__(self):
        self.__tv = None 

    def setTv(self, tv):
        self.__tv = tv

    def turnOn(self):
        if self.__tv:
            self.__tv.turnOn()

    def canalUp(self):
        if self.__tv:
            self.__tv.canalUp()

    def setCanal(self, canal: int):
        if self.__tv:
            self.__tv.setCanal(canal)

    def enlazar(self, tv):
        self.__tv = tv
        tv.setControl(self) 

    def turnOff(self):
        if self.__tv:
            self.__tv.turnOff()

    def volumenDown(self):
        if self.__tv:
            self.__tv.volumenDown()

    def volumenUp(self):
        if self.__tv:
            self.__tv.volumenUp()

    def canalDown(self):
        if self.__tv:
            self.__tv.canalDown()

    def getTv(self):
        return self.__tv

    def setVolumen(self, volumen: int):
        if self.__tv:
            self.__tv.setVolumen(volumen)