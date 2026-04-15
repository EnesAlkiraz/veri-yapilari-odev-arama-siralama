# veri-yapilari-odev-arama-siralama
Veri Yapıları Ve Algoritma dersi arama ve sıralama algoritmaları projesi
Searching & Sorting Algorithms (Python)

Bu proje, temel arama ve sıralama algoritmalarını Python ile implement etmek ve performanslarını karşılaştırmak amacıyla hazırlanmıştır.

İçerik

Projede aşağıdaki algoritmalar bulunmaktadır:

Arama Algoritmaları
Linear Search (Doğrusal Arama)
Binary Search (İkili Arama)
Jump Search (Sıçramalı Arama)
Sıralama Algoritmaları
Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Shell Sort
Proje Yapısı
algorithms.py


Tek dosyada tüm algoritmalar ve test senaryoları bulunmaktadır.

Nasıl Çalıştırılır?

Python 3 yüklü olması yeterlidir.

python algorithms.py

Örnek Çıktı

Program çalıştırıldığında:

Orijinal liste
Sıralanmış versiyonlar
Arama sonuçları
Performans karşılaştırmaları

ekrana yazdırılır.

Performans Karşılaştırması
Algoritma	Zaman Karmaşıklığı
Bubble Sort	O(n²)
Selection Sort	O(n²)
Insertion Sort	O(n²)
Merge Sort	O(n log n)
Quick Sort	O(n log n) (ortalama)
Shell Sort	O(n log n) ~ O(n²)
Linear Search	O(n)
Binary Search	O(log n)
Jump Search	O(√n)
Amaç

Bu proje şunları öğretmeyi hedefler:

Algoritmaların temel mantığını anlamak
Arama ve sıralama tekniklerini karşılaştırmak
Zaman karmaşıklığını pratikte görmek
Python’da temiz ve modüler kod yazımı
Öğrenilen Konular
Listeler üzerinde işlem yapma
Rekürsif (recursive) algoritmalar
Zaman ölçümü (time modülü)
Big-O notasyonu mantığı
Algoritma karşılaştırma teknikleri
Notlar
Tüm sıralama fonksiyonları orijinal listeyi korumak için .copy() kullanır.
Quick Sort ve Merge Sort recursive yapı kullanır.
Jump Search algoritması sıralı liste gerektirir.
Geliştiren

Bu proje eğitim amaçlı geliştirilmiştir.

