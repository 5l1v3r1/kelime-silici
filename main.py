dosyaadi = str(input("Dosya adınızı giriniz.\nDosya adı: ")) # Dosya adını alıyoruz.
dosyaadi = str(dosyaadi + ".txt") # Dosya adının sonuna .txt ekliyoruz.

with open(dosyaadi, 'r') as dosya: # Dosyamızı açıyoruz.
  dosyaverisi = dosya.read()

silincek = str(input("Silinecek kelime: ")) # Dosyamızdan silinecek kelimeyi alıyoruz.
dosyaverisi = dosyaverisi.replace(silincek, '') # Kelimeyi siliyoruz.
baska = str(input("E/H Sorusu\nBaşka kelime silmek ister misiniz?")) # Başka silmek istediği var mı diye soruyoruz.

if baska == "E": # Evet seçtiyse aşağıdaki kodu çalıştırıyoruz.
    silincek2 = str(input("Silinecek kelime: ")) # Silinecek kelimeyi tekrar soruyoruz.
    dosyaverisi = dosyaverisi.replace(silincek2, '') # Kelimeyi tekrardan siliyoruz.
    print("Başarıyla", silincek, "ve", silincek2, "silindi!") # Sildiğimize dair çıktı veriyoruz.
else: # Hayır seçtiyse aşağıdaki kodu çalıştırıyoruz.
    print("Başarıyla", silincek, "Silindi!") # Sildiğimize dair çıktı veriyoruz.

with open(dosyaadi, 'w') as dosya:
  dosya.write(dosyaverisi)
