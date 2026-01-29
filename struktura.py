import nazwy
naz = nazwy.nazwy()
class Struktura:
    def __init__(self,typ,id):
        self.typ = typ
        self.id = id
        self.czy_zamknieta = False
        self.elementy = []
        self.zajeta =False
        if self.typ == naz.POLE:
            self.miasta_na_polu = set()


        self.punkty = 0
        self.pionki = None
    def dodaj_element(self, x_grid, y_grid, nowy_id,poloczenia):
        self.elementy.append((x_grid,y_grid,nowy_id,poloczenia))
    def scal(self, nowa_strukt):
        self.elementy.extend(nowa_strukt.elementy)
    def dodaj_punkty(self,gracze):
        zwyciesca = self.znajdz_zwyciezce()
        
        
        if zwyciesca is not None:
            for gracz in gracze:
                if gracz in zwyciesca:

            
                    gracz.punkty += self.punkty
                    
                     #do zrobienia klasa gracz z iloscia punktow
    def znajdz_zwyciezce(self):
        maxi = 0
        zwyciesca = None
       
        if self.zajeta is not False:
            for gracz in self.zajeta:
                ilosc = self.zajeta.count(gracz)
                
                if ilosc > maxi:
                    zwyciesca =[gracz]
                    maxi = ilosc
                elif ilosc == maxi and ilosc != 0:
                    zwyciesca.append(gracz)    
        return zwyciesca     