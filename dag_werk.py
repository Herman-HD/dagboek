from datetime import datetime
import sys

def lees_die_lêer():
    with open("/Users/User/Dropbox/Python/SANDBOX/dagboek/dagboek.txt", "r") as gestoorde_data:
        gestoorde_lyne = gestoorde_data.readlines()
    return gestoorde_lyne

class MyDag():
    alle_werk = []
    laaste_nommer = 0
    teller = 0
    input_str = "[(>)  gestoor(-3)\t(<)  opgeneem\n (/)  alles\t\t(**) verwyder \n (++) stoor]\n[Gedoen : > "
## maak seker leer bestaan
    with open("/Users/User/Dropbox/Python/SANDBOX/dagboek/dagboek.txt", "a") as data_lêer:
        data_lêer.write("")
## en lees die leer
    lines = lees_die_lêer()
    if lines == []:
        laaste_nommer = 0
    else:
        laaste_datum = str(lines[-1].split(", ")[0])[1:]
        laaste_nommer = int(str(lines[-1].split(", ")[1]))
        laaste_werk = str(lines[-1].split(", ")[2])[:-2]

    def __init__(self, werk=input(input_str)):
        self.alle_werk = MyDag.alle_werk
        nou = datetime.now()
        self.datum = nou.strftime("%d/%m/%Y %H:%M")
        self.werk = werk
        while not None:
            if self.werk == "?":
                print(self)
            elif self.werk == ">":
                self.laaste_drie_oplêer()
            elif self.werk == "<":
                self.laaste_opgeneem()
            elif self.werk == "/":
                self.alle_data()
            elif self.werk == "**":
                self.verwyder_laaste()
            elif self.werk == "++":
                self.skryf_items()
                self.alle_werk = []
            elif all([True if x == " " else False for x in [*self.werk]]) or self.werk == "":
                self.skryf_items()
                sys.exit()
                return None
            else:
                self.voeg_item_by()
            self.werk=input(MyDag.input_str)

    def laaste_drie_oplêer(self):
        lyne = lees_die_lêer()
        if len(lyne) < 1:
            print("Geen data gestoor")
        else:
            for item in [-3, -2, -1]:
                print(f"{lyne[item]}", end="")
        return True

    def laaste_opgeneem(self):
        if len(MyDag.alle_werk) >= 3:
            print(f"{MyDag.alle_werk[-3]}\n{MyDag.alle_werk[-2]}\n{MyDag.alle_werk[-1]}")
        elif len(MyDag.alle_werk) == 2:
            print(f"{MyDag.alle_werk[-2]}\n{MyDag.alle_werk[-1]}")
        elif len(MyDag.alle_werk) == 1:
            print(f"{MyDag.alle_werk[-1]}")
        else:
            print("  Skoon !")
        return True

    def laaste_nom(self):
        lyne = lees_die_lêer()
        if lyne == "":
            MyDag.laaste_nommer = 0
        else:
            MyDag.laaste_nommer = int(str(lyne[-1].split(", ")[1]))
        return MyDag.laaste_nommer

    def alle_data(self):
        lyne = lees_die_lêer()
        for item in lyne:
            print(item.replace("\n", ""))
        for werk in list(MyDag.alle_werk):
            print(werk)
        return True

    def verwyder_laaste(self):
        if len(MyDag.alle_werk) < 1:
            data = lees_die_lêer()[:-1]
            with open("/Users/User/Dropbox/Python/SANDBOX/dagboek/dagboek.txt", "w", encoding="UTF-8") as rw_data:
                for item in data:
                    rw_data.write(item)
            self.laaste_nom()
        else:
            MyDag.alle_werk = MyDag.alle_werk[:-1]
            MyDag.teller = 0 if MyDag.teller <= 0 else MyDag.teller - 1
        return True
                
    def skryf_items(self):
        with open("/Users/User/Dropbox/Python/SANDBOX/dagboek/dagboek.txt", "a", encoding="UTF-8") as leer1:#,\
            for item in MyDag.alle_werk:
                leer1.write(f"[{item[0]}, {item[1]}, {item[2]}]\n")
        MyDag.alle_werk = []
        MyDag.teller = 0
        self.laaste_nom()
        return True

    def voeg_item_by(self):
        self.laaste_nom()
        MyDag.teller += 1
        MyDag.alle_werk.append([self.datum, int(MyDag.laaste_nommer)+MyDag.teller, self.werk])
        print(f"{self.datum}  werk: {self.werk}  no: {int(MyDag.laaste_nommer)+MyDag.teller}")
        return True

    def __str__(self):
        return f"{self.datum}  werk: {self.werk}  no: {int(MyDag.laaste_nommer)+MyDag.teller}"

my_toep = MyDag()#werk=input("[ Gedoen : > "))
