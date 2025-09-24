def boy_kilo_endeksi():
    boy = float(input("Boyunuzu metre cinsinden giriniz: "))
    kilo = float(input("Kilonuzu giriniz: "))
    endeks = kilo / (boy * boy)

    if 18.5 <= endeks <= 24.9:
        print("Sağlıklı")
    elif endeks > 24.9:
        print("Kilolu")
    else:
        print("Zayıf")


