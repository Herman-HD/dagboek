from datetime import datetime
from leers.tools import l_tools as lts
import sys, time

class dagboek:
    n_objects = 0
    
    def __init__(self):
## inisialiseer veranderlikes
        self.werk = ""
        self.alle_werk = []
        self.lyne = []
        self.teller = 0
        self.datum = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.input_str = "[(>)  gestoor(-3)\t(<)  opgeneem\n (/)  alles\t\t(**) verwyder \n (++) stoor\t\t(?)  nommer]\n[Gedoen : > "
## maak seker data leer bestaan
        self.leer = lts("dagboek.txt")
        self.leer.init_leer()
## en lees die leer
        self.lyne = self.leer.lees_leer()
## stel veranderlikes op vir gebruik
        if self.lyne == []:
            self.laaste_nommer = 0
            self.laaste_datum = datetime.now().strftime("%d/%m/%Y %H:%M")
        else:
            self.laaste_datum = str(self.lyne[-1].split(", ")[0])[1:]
            self.laaste_nommer = int(str(self.lyne[-1].split(", ")[1]))
            self.laaste_werk = str(self.lyne[-1].split(", ")[2])[:-2]        

## besluit hoeveel instansies van die objek beskikbaar is (2)
    def __new__(cls):
        if cls.n_objects < 2:
            cls.n_objects += 1
            return object.__new__(cls)
        return f"Net 2 objekte beskikbaar."

## lees laaste 3 items op gestoorde data    
    def laaste_drie_opleer(self):
        self.lyne = self.leer.lees_leer()
        if len(self.lyne) < 1:
            print("\n\tGeen data gestoor!")
        else:
            for item in [-3, -2, -1]:
                print(f"{lyne[item]}", end="")
        return True

## kyk wat is huidiglik opgeneem tot 3 records terug
    def laaste_opgeneem(self):
        if len(self.alle_werk) >= 3:
            print(f"{self.alle_werk[-3]}\n{self.alle_werk[-2]}\n{self.alle_werk[-1]}")
        elif len(self.alle_werk) == 2:
            print(f"{self.alle_werk[-2]}\n{self.alle_werk[-1]}")
        elif len(self.alle_werk) == 1:
            print(f"{self.alle_werk[-1]}")
        else:
            print("\n\tSkoon !")
        return True

## kry laaste nommer van gestoorde data
    def laaste_nom(self):
        self.lyne = self.leer.lees_leer()
        if self.lyne == "" or self.lyne == []:
            self.laaste_nommer = 0
        else:
            if datetime.strptime(self.datum.split(" ")[0], "%d/%m/%Y") > datetime.strptime(self.laaste_datum.split(" ")[0], "%d/%m/%Y"):
                self.laaste_nommer = 0
            else:
                self.laaste_nommer = int(str(self.lyne[-1].split(", ")[1]))
        return self.laaste_nommer

## kry alle data gestoor en in geheue
    def alle_data(self):
        self.lyne = self.leer.lees_leer()
        for item in self.lyne:
            print(item.replace("\n", ""))
        for werk in list(self.alle_werk):
            print(werk)
        return True

## skrap laaste item in alle data
    def verwyder_laaste(self):
        if len(self.alle_werk) < 1:
            data = self.leer.lees_leer()[:-1]
            self.leer.oorskryf_leer(data)
            self.laaste_nom()
        else:
            self.alle_werk = self.alle_werk[:-1]
            self.teller = 0 if self.teller <= 0 else self.teller - 1
        return True

## skryf ingeleesde data na leer                
    def skryf_items(self):
        self.leer.voegby_leer(self.alle_werk)
        self.alle_werk = []
        self.teller = 0
        self.laaste_nom()
        return True

## voeg 1 item by in geheue
    def voeg_item_by(self):
        self.laaste_nom()
        self.teller += 1
        self.alle_werk.append([self.datum, int(self.laaste_nommer)+self.teller, self.werk])
        print(f"{self.datum}  werk: {self.werk}  no: {int(self.laaste_nommer)+self.teller}")
        return True

## wat is laaste opgeneem
    def __str__(self):
        return f"{self.datum}  werk: {self.werk}  no: {int(self.laaste_nommer)+self.teller+1}"

## kieslys
    def kies_lys(self):
        self.werk = input(self.input_str)
        while True:
##            print("Objects = ", self.n_objects)
            self.datum = datetime.now().strftime("%d/%m/%Y %H:%M")
            if self.werk == "?":
                print(self)
            elif self.werk == ">":
                self.laaste_drie_opleer()
            elif self.werk == "<":
                self.laaste_opgeneem()
            elif self.werk == "/":
                self.alle_data()
            elif self.werk == "**":
                self.verwyder_laaste()
            elif self.werk == "++":
                self.skryf_items()
            elif all([True if x == " " else False for x in [*self.werk]]) or self.werk == "":
                self.skryf_items()
                print("\n\t Program gestaak...")
                time.sleep(1)
                sys.exit()
            else:
                self.voeg_item_by()
            self.werk=input(self.input_str)

if __name__ == "__main__":
    run_me = dagboek()
    run_me.kies_lys()

