import nazwy
import arcade
naz = nazwy.nazwy()

class Pionek:
    def __init__(self, kolor= None, pozycja = None, kafelek = None,kat = None):
        self.kolor = kolor
        self.pozycja_na_kafelku = pozycja
        self.zajety_kafelek = kafelek
        self.kat = kat
        self.sprite = None
        self.x = None
        self.y = None
        
        self.sciezka = r"E:\__priv\python\__pv\carcasonne\pionki/" +self.kolor+".png"
    
    def do_sprite(self,x_center =None,y_center=None):
        if x_center is None:
            x_center, y_center = self.x, self.y
        sprite = arcade.Sprite(self.sciezka, scale=0.1, center_x=x_center, center_y=y_center)
        sprite.angle = self.kat
        self.sprite = sprite
        return sprite
        
        


        pass