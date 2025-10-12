ilaclar=[]

günlük_ilaclar = {
    "tansiyon ilaçları": ["coversyl", "kaptoril", "rilace", "delix"],
    "ağrı ilaçları": ["parol", "apravax", "arvales"]

}
tum_ilaclar = ["coversyl", "kaptoril", "rilace", "delix", 
               "parol", "apravax", "arvales"]

alınan= input('alınan ilaçlar virgül ile giriniz')
alınan_ilaclar = [i.strip().lower() for i in alınan.split(",")]
for ilac in tum_ilaclar:
    if ilac in alınan_ilaclar:
        print(ilac, "✅ alındı")
    else:
        print(ilac, "❌ alınmadı")
eksikler=[]
for ilac in tum_ilaclar :
    if ilac not in alınan_ilaclar:
     eksikler.append(ilac) 
with open("ilac_kontrol.txt", "w", encoding="utf-8") as f:
    f.write("Bugünkü ilaç kontrolü:\n")
    f.write("Alınan ilaçlar:\n")
    for ilac in alınan_ilaclar:
        f.write(f"- {ilac}\n")
    f.write("\nEksik ilaçlar:\n")
    for ilac in eksikler:
        f.write(f"- {ilac}\n")

