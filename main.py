dosyaadi = str(input("Dosya adınızı giriniz.\nDosya adı: ")) # Dosya adını alıyoruz.
dosyaadi = str(dosyaadi + ".txt") # Dosya adının sonuna .txt ekliyoruz.

with open(dosyaadi, 'r') as dosya: # Dosyamızı açıyoruz.
  dosyaverisi = dosya.read()

silincek = str(input("Silinecek kelime: ")) # Dosyamızdan silinecek kelimeyi alıyoruz.
dosyaverisi = dosyaverisi.replace(silincek, '') # Kelimeyi siliyoruz.
print("-"*50)
baska = str(input("E/H Sorusu\nBaşka kelime silmek ister misiniz?")) # Başka silmek istediği var mı diye soruyoruz.
print("-"*50)

while baska == "E":
    silincek2 = str(input("Silinecek kelime: ")) # Silinecek kelimeyi tekrar soruyoruz.
    dosyaverisi = dosyaverisi.replace(silincek2, '') # Kelimeyi tekrardan siliyoruz.
    print("-"*50)
    print("Başarıyla verilen kelime/kelimeler silindi!") # Sildiğimize dair çıktı veriyoruz.
    print("-"*50)
    baska = str(input("E/H Sorusu\nBaşka kelime silmek ister misiniz?"))

print("-"*50)
print("Başarıyla verilen kelime/kelimeler silindi!") # Sildiğimize dair çıktı veriyoruz.
print("-"*50)   
print("Programdan çıkılıyor..")
#if baska == "E": # Evet seçtiyse aşağıdaki kodu çalıştırıyoruz.
#    silincek2 = str(input("Silinecek kelime: ")) # Silinecek kelimeyi tekrar soruyoruz.
#    dosyaverisi = dosyaverisi.replace(silincek2, '') # Kelimeyi tekrardan siliyoruz.
#    print("Başarıyla", silincek, "ve", silincek2, "silindi!") # Sildiğimize dair çıktı veriyoruz.

with open(dosyaadi, 'w') as dosya:
  dosya.write(dosyaverisi)
