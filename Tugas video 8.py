# REFERENSI SOAL : UG 8 KELAS C D
# TEMA: Membaca dan Menulis File.

# Pada suatu hari, Rocky sedang menghitung jumlah ayam goreng yang akan dijualnya.
# Namun menurut angka hoki angka yang akan membawa keberuntungan untuk si Rocky adalah angka prima,
# Tanpa lama-lama berhitung, Rocky meminta kamu sebagai programmer untuk
# memunculkan deret dari angka prima yang sampai dengan angka yg dimasukkan oleh Rocky,
# sebagai acuan Rocky untuk menggoreng ayam. Kemudian akan disimpan dalam File angka.txt,
# sebagai programmer, bantulah Rocky untuk membuat program tersebut.
# input : 8
# output: 2 ekor 3 ekor 5 ekor 7 ekor 

#Input
angka_hoki=int(input("Masukkan angka hoki Rocky: "))

#Bikin File untuk Menulis'
file_hoki=open("Angka Hoki Rocky.txt","w")

#Proses
for angka in range (1,angka_hoki+1):
    #bilangan prima >1
    if angka>1:
        for bilangan in range (2,angka):
            if angka%bilangan==0:
                break
        else:
            #Menulis teks
            #Output
            angka1=str(angka)
            teks=angka1 + " ekor "
            file_hoki.write(teks)

#Close File
file_hoki.close()