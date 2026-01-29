class nazwy:
    def __init__(self):
        self.MIASTO = "miasto"
        self.DROGA = "droga"
        self.POLE  = "pole"
        self.KLASZTOR = "klasztor"
        self.N = "N"
        self.S = "S"
        self.E = "E"
        self.W = "W"
        self.CENTER = "center"
# Północ (North)
        self.NL = "N_L" # Północ - Lewo
        self.NP = "N_P" # Północ - Prawo
        
        # Południe (South)
        self.SL = "S_L" # Południe - Lewo
        self.SP = "S_P" # Południe - Prawo
        
        # Wschód (East) - tu używamy Góra/Dół
        self.EG = "E_G" # Wschód - Góra
        self.ED = "E_D" # Wschód - Dół
        
        # Zachód (West) - tu używamy Góra/Dół
        self.WG = "W_G" # Zachód - Góra
        self.WD = "W_D" # Zachód - Dół

        # --- Mapa połączeń (Słownik Przeciwieństw) ---
        # Określa, co z czym się styka na planszy.
        self.OPOZYTY_POLA = {
            # Północ łączy się z Południem (Lewo do Lewego, Prawo do Prawego)
            self.NL: self.SL,
            self.NP: self.SP,
            self.SL: self.NL,
            self.SP: self.NP,
            
            # Wschód łączy się z Zachodem (Góra do Góry, Dół do Dołu)
            self.EG: self.WG,
            self.ED: self.WD,
            self.WG: self.EG,
            self.WD: self.ED,
            self.N: self.S,
            self.S: self.N,
            self.E: self.W,
            self.W:self.E



        }




class fazy:
    def __init__(self):
        
        self.KAFELEK = "stawianie_kafelka"
        self.PIONEK = "stawianie_pionka"
        self.ZMIANA = "zmiana_gracza"