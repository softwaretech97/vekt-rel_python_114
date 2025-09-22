def gezilen_yerler(): 
    print("╔════════════════════════════════╗")
    print("║       LEVİATHAN APP            ║")
    print("║  1- Gezilen Yerler             ║")
    print("║     A-Kapadokya                ║")
    print("║     B-Sultan Ahmet Cami        ║")
    print("║     C-Kapalı Çarşı             ║")
    print("║     D-Ulu Çarşı                ║")
    print("╚════════════════════════════════╝")

    secim1 = input("Nereyi Gezdin? ").upper()         

    if secim1 == "A":
        print('''Kapadokya, Türkiye’nin Nevşehir, Aksaray, Niğde, Kayseri ve Kırşehir illerini kapsayan tarihi bir bölgedir.
Bölge; peribacaları, yeraltı şehirleri ve kayalara oyulmuş kiliseleriyle ünlüdür.
Tarihi boyunca Hititler, Persler, Romalılar ve Bizanslılar gibi birçok medeniyete ev sahipliği yapmıştır.
UNESCO Dünya Mirası Listesi’nde yer alır ve her yıl milyonlarca turist çeker.''')

    elif secim1 == "B":
        print('''Sultan Ahmet Camii, 1609-1617 yılları arasında Osmanlı padişahı I. Ahmed tarafından İstanbul’da yaptırılmıştır.
Mavi çinileri nedeniyle yabancılar tarafından “Blue Mosque” olarak da bilinir.
Hem cami hem de külliye olarak tasarlanmış olup Ayasofya’nın karşısında, İstanbul’un en önemli tarihi yapılarından biridir.''')

    elif secim1 == "C":
        print('''İstanbul’daki Kapalıçarşı, 15. yüzyılda Fatih Sultan Mehmet döneminde kurulmuş dünyanın en eski ve en büyük çarşılarından biridir.
İçinde yaklaşık 4.000 dükkân bulunur ve sokaklarının toplam uzunluğu 60 kilometreyi bulur.
Altın, halı, baharat, antika ve el sanatlarıyla ünlüdür; her gün binlerce yerli ve yabancı turisti ağırlar.''')

    elif secim1 == "D":
        print('''Bursa Ulu Cami, 1399 yılında Yıldırım Bayezid tarafından yaptırılmış ve Osmanlı’nın erken dönem mimarisinin en önemli eserlerinden biridir.
20 kubbesi, hat sanatının eşsiz örnekleri ve tarihi atmosferiyle Türkiye’nin en önemli camilerinden sayılır.''')

    else:
        print("Geçersiz seçim!")
