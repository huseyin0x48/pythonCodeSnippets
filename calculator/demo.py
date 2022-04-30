giriş = """
(1) Topla
(2) Çıkar
(3) Çarp
(4) Böl
(5) Üstünü Al
(6) Kökünü Al
"""

print(giriş)

soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

if soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı giriniz: "))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
    print(sayı1, "+", sayı2, "=", sayı1+sayı2)

elif soru == "2":
    sayı1 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
    sayı2 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
    print(sayı1, "-", sayı2, "=", sayı1-sayı2)

elif soru == "3":
    sayı1 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayı2 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
    print(sayı1, "x", sayı2, "=", sayı1*sayı2)

elif soru == "4":
    sayı1 = int(input("Bölme işlemi için ilk sayıyı giriniz: "))
    sayı2 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayı1, "÷", sayı2, "=", sayı1/sayı2)

elif soru == "5":
    sayı1 = int(input("Üst alma işlemi için sayıyı giriniz: "))
    sayı2 = int(input("Üstün derecesini giriniz: "))
    print(sayı1, "^", sayı2, "=", sayı1**sayı2)


elif soru == "6":
    sayı1 = int(input("Kök alma işlemi için sayıyı giriniz: "))
    sayı2 = int(input("Kökün derecesini giriniz: "))
    print(sayı1, "sayısının", sayı2, ". dereceden kökü =", pow(sayı1, 1/sayı2))

else:
    print("Geçerli bir işlem giriniz.", giriş)