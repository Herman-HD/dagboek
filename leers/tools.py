import os
class l_tools:

    def __init__(self, leer_naam):
        self.leer = os.getcwd()+"\\"+leer_naam

    def lees_leer(self):
        with open(self.leer, "r") as lr:
            return lr.readlines()

    def init_leer(self):
        with open(self.leer, "a") as nl:
            nl.write("")
    
    def oorskryf_leer(self, data):
        with open(self.leer, "w", encoding="UTF-8") as osl:
            for item in data:
                osl.write(item)

    def voegby_leer(self, items):
        with open(self.leer, "a", encoding="UTF-8") as vbl:
            for item in items:
                vbl.write("{}\n".format(str(item).replace("'", "")))
