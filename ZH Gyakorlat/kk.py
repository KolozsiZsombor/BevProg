class Szuperhos:
    def __init__(self, nev, szuperero=50):
        self._nev = nev 
        self._szuperero = szuperero


    @property
    def szuperero(self):            # get property
        return self._szuperero

    @szuperero.setter
    def szuperero(self, ertek):     # set property
        self._szuperero = ertek
        
    def __str__(self):
        return self._nev + " egy szuperhős, akinek szuperereje " + str(self._szuperero)

    # két szuperhős akkor lesz egyenlő, ha a nevük és a szupererejük megegyezik

    def __eq__(self, masik_hos):
        return self._nev == masik_hos._nev and self._szuperero == masik_hos._szuperero

    # két szuperhős összeadása során a szupererejük összeadódik

    def __add__(self, masik_hos):
        if isinstance(masik_hos, Szuperhos):   # típusellenőrzés
            uj_szuperero = self._szuperero + masik_hos._szuperero
            uj_szuperhos = Szuperhos("Megahős", uj_szuperero)
            return uj_szuperhos
        else:
            print("Egy szuperhőst csak egy másik szuperhőssel lehet összeadni.")

# === tesztelés ===

hos1 = Szuperhos("Thor", 70)
hos2 = Szuperhos("Hulk", 80)
hos3 = Szuperhos("Hulk", 80)
hos4 = hos1 + hos2
print(hos2 == hos3)
print(hos4)  