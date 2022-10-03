class Szuperhos:
    def __init__(self, nev, szuperero = 50):
        self._nev = nev
        self._szuperero = szuperero 
        # print("--Szuperhős létrehozva--")

    @property
    def szuperero(self):
        return self._szuperero

    @szuperero.setter
    def szuperero(self, ertek):
        self._szuperero = ertek

    def __str__(self):
        return self._nev + f"Egy szuperhős, akinkek a szuperereje {str(self._szuperero)} "

hos1 = Szuperhos("Thor",70)

print(hos1)