
class Hesap:
    def __init__(self,sayı1,sayı2):
        self.sayı1=sayı1
        self.sayı2=sayı2
    def carp(self):
        toplam=self.sayı1*self.sayı2
        return toplam
    def bol(self):
        toplam=self.sayı1/self.sayı2
        return toplam
    def topla(self):
        toplam=self.sayı1+self.sayı2
        return toplam
    def cıkar(self):
        toplam=self.sayı1-self.sayı2
        return toplam
    def yazdır(self):
        carpma=self.carp()
        toplama=self.topla()
        cıkar=self.cıkar()
        bol=self.bol()

    