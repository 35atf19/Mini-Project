giriş = """ Seçmek isteğiniz rakama basınız.
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) karesini Alma
(6) Karekökü Alma
"""
soru = input("Yapmak istedğiniz işlemin numarasını girin:")

if soru == "1":
    sayı1 = int(input("Toplama işlemiAA yapmak için ilk sayıyı giriniz:"))
    sayı2 = int(input("Toplama işlemi yapmak için ikinci sayıyı giriniz:"))
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
elif soru == "2":
    sayı3 = int(input("Çıkarma işlemi yapmak için ilk sayıyı giriniz:"))
    sayı4 = int(input("Çıkarma işlemi yapmak için ikinci sayıyı giriniz:"))
    print(sayı3,"-", sayı4, "=", sayı3 - sayı4)
elif soru == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı giriniz:"))
    sayı6 = int(input("Çarpma işemi için ikinci sayıyı giriniz:"))
    print(sayı5, "x",sayı6, "=", sayı5*sayı6)
elif soru == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı giriniz:"))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı giriniz:"))
    print(sayı7, "/", sayı8, "=", sayı7/sayı8)
elif soru == "5":
    sayı9 = int(input("Karesini almak istediğiniz sayıyı giriniz:"))
    print(sayı9, "x", sayı9,"=", sayı9**2)
elif soru == "6":
    sayı10 = int(input(("Karekökünü almak istedğiniz sayıyı giriniz:")))
    print(sayı10**0.5)    
