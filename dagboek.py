from datetime import datetime
from leers.tools import l_tools as lts
import sys, time

class dagboek:
    n_objects = 0
    
    def __init__(self):
        self.werk = ""
        self.alle_werk = []
        self.teller = 0
        self.datum = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.input_str = "[(>)  gestoor(-3)\t(<)  opgeneem\n (/)  alles\t\t(**) verwyder \n (++) stoor\t\t(?)  nommer]\n[Gedoen : > "
## maak seker data leer bestaan
        self.leer = lts("dagboek.txt")
        self.leer.init_leer()
## en lees die leer
        lyne = self.leer.lees_leer()
        if lyne == []:
            self.laaste_nommer = 0
        else:
            self.laaste_datum = str(lyne[-1].split(", ")[0])[1:]
            self.laaste_nommer = int(str(lyne[-1].split(", ")[1]))
            self.laaste_werk = str(lyne[-1].split(", ")[2])[:-2]        

    def __new__(cls):
        if cls.n_objects < 2:
            cls.n_objects += 1
            return object.__new__(cls)
        return None
    
    def laaste_drie_opleer(self):
        lyne = self.leer.lees_leer()
        if len(lyne) < 1:
            print("Geen data gestoor")
        else:
            for item in [-3, -2, -1]:
                print(f"{lyne[item]}", end="")
        return True

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

    def laaste_nom(self):
        lyne = self.leer.lees_leer()
        if lyne == "" or lyne == []:
            self.laaste_nommer = 0
        else:
            if datetime.strptime(self.datum.split(" ")[0], "%d/%m/%Y") > datetime.strptime(self.laaste_datum.split(" ")[0], "%d/%m/%Y"):
                self.laaste_nommer = 0
            else:
                self.laaste_nommer = int(str(lyne[-1].split(", ")[1]))
        return self.laaste_nommer

    def alle_data(self):
        lyne = self.leer.lees_leer()
        for item in lyne:
            print(item.replace("\n", ""))
        for werk in list(self.alle_werk):
            print(werk)
        return True

    def verwyder_laaste(self):
        if len(self.alle_werk) < 1:
            data = self.leer.lees_leer()[:-1]
            self.leer.oorskryf_leer(data)
            self.laaste_nom()
        else:
            self.alle_werk = self.alle_werk[:-1]
            self.teller = 0 if self.teller <= 0 else self.teller - 1
        return True
                
    def skryf_items(self):
        self.leer.voegby_leer(self.alle_werk)
        self.alle_werk = []
        self.teller = 0
        self.laaste_nom()
        return True

    def voeg_item_by(self):
        self.laaste_nom()
        self.teller += 1
        self.alle_werk.append([self.datum, int(self.laaste_nommer)+self.teller, self.werk])
        print(f"{self.datum}  werk: {self.werk}  no: {int(self.laaste_nommer)+self.teller}")
        return True

    def __str__(self):
        return f"{self.datum}  werk: {self.werk}  no: {int(self.laaste_nommer)+self.teller+1}"

    def kies_lys(self):
        self.werk = input(self.input_str)
        while True:
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
                time.sleep(2)
                sys.exit()
            else:
                self.voeg_item_by()
            self.werk=input(self.input_str)

if __name__ == "__main__":
    run_me = dagboek()
    run_me.kies_lys()
