class Hesap:
    def sec(self):
        secim = int(input("1-Toplama\n2-Çarpma\n3-Çıkarma\n4-Bölme\n\nSeç: "))

        if secim == 1:
            self.topla()

        if secim == 2:
            self.carpma()
        
        if secim == 3:
            self.cıkarma()

        if secim == 4:
            self.bolme
            
    
    def topla(self):
        ilk_sayi = int(input("Sayı gir: "))
        ikinci_sayi = int(input("Sayı gir: "))
        
        print(ilk_sayi+ikinci_sayi)    

    def carpma(self):
        ilk_sayi = int(input("Sayı gir: "))
        ikinci_sayi = int(input("Sayı gir: "))
        
        print(ilk_sayi*ikinci_sayi)

    def cıkarma(self):
        ilk_sayi = int(input("Sayı gir: "))
        ikinci_sayi = int(input("Sayı gir: "))

        print(ilk_sayi-ikinci_sayi)

    def bolme(self):
        ilk_sayi= int(input("Sayı gir: "))        
        ikinci_sayi= int(input("Sayı gir: "))

        print(ilk_sayi//ikinci_sayi)

hesap=Hesap()
hesap.sec()


