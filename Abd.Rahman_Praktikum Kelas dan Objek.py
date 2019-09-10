class lingkaran:
    def __init__(self):
        print("Kontruktor Lingkaran dipanggil")
        self.r=int(input("masukkan jari-jari = "))
    def __del__(self):
        print("Kontruktor Lingkaran dipanggil")
    def luaslingkaran(self):
        phi=3.14
        luas=phi*self.r**2
        print("luas lingkaran\t     : ",luas)
    def keliling(self):
        phi=3.14
        kel=2*phi*self.r
        print("keliling lingkaran\t : ",kel)
        print("Kontruktor Lingkaran dipanggil")
                
a=lingkaran()
a.luaslingkaran()
a.keliling()
