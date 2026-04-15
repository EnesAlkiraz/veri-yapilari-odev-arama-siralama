# veri-yapilari-odev-arama-siralama
Veri Yapıları Ve Algoritma dersi arama ve sıralama algoritmaları projesi
#Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları
Proje Amacı

Bu projede farklı arama ve sıralama algoritmalarının Python dili ile uygulanması, çalışma mantıklarının anlaşılması ve performanslarının karşılaştırılması amaçlanmıştır.

Arama Algoritmaları
Linear Search (Doğrusal Arama)
Listenin başından başlayarak tüm elemanları tek tek kontrol eder.
Sıralı olma şartı yoktur.
Zaman Karmaşıklığı: O(n)
Binary Search (İkili Arama)
Listeyi sürekli ikiye bölerek arama yapar.
Sadece sıralı listelerde çalışır.
Zaman Karmaşıklığı: O(log n)
Jump Search (Adımlamalı Arama)
Liste üzerinde belirli aralıklarla (√n) zıplayarak ilerler.
Uygun blok bulunduğunda doğrusal arama yapar.
Zaman Karmaşıklığı: O(√n)
Sıralama Algoritmaları
Bubble Sort
Komşu elemanları karşılaştırarak büyük olanı sağa iter.
Basit ama büyük verilerde yavaştır.
Zaman Karmaşıklığı: O(n²)
Selection Sort
Her adımda en küçük elemanı seçip başa yerleştirir.
Zaman Karmaşıklığı: O(n²)
Insertion Sort
Elemanları doğru konuma yerleştirerek sıralar.
Küçük veri setlerinde etkilidir.
Zaman Karmaşıklığı: O(n²)
Merge Sort
Böl ve fethet mantığıyla çalışır.
Listeyi parçalara ayırır ve sıralı şekilde birleştirir.
Zaman Karmaşıklığı: O(n log n)
Space Complexity: O(n)
Quick Sort
Pivot seçerek listeyi ikiye böler.
Ortalama durumda çok hızlıdır.
Zaman Karmaşıklığı: O(n log n)
Space Complexity: O(n)
Shell Sort
Insertion Sort’un geliştirilmiş halidir.
Belirli aralıklarla karşılaştırma yapar.
Zaman Karmaşıklığı: O(n log n) ile O(n²) arası
Algoritmaların Karşılaştırılması
Algoritma	Tür	Zaman Karmaşıklığı
Linear Search	Arama	O(n)
Binary Search	Arama	O(log n)
Jump Search	Arama	O(√n)
Bubble Sort	Sıralama	O(n²)
Selection Sort	Sıralama	O(n²)
Insertion Sort	Sıralama	O(n²)
Merge Sort	Sıralama	O(n log n)
Quick Sort	Sıralama	O(n log n)
Shell Sort	Sıralama	O(n log n) - O(n²)
Performans Analizi

Kod içerisinde time modülü kullanılarak her sıralama algoritmasının çalışma süresi ölçülmektedir.

Genel Sonuçlar
Basit algoritmalar (Bubble, Selection, Insertion) büyük verilerde yavaştır.
Gelişmiş algoritmalar (Merge, Quick, Shell) daha hızlıdır.
Quick Sort ve Merge Sort genelde en iyi performansı gösterir.
Nasıl Çalıştırılır
Python yüklü olmalıdır.
Dosyayı indiriniz.
Terminal veya VS Code üzerinden çalıştırınız:
python dosya_adi.py

Örnek Çıktı

Program çalıştırıldığında:

Orijinal liste ekrana yazdırılır
Tüm sıralama algoritmaları çalışır
Arama algoritmaları indeks döndürür
Performans karşılaştırması ekrana basılır
Not

Bu proje eğitim amaçlı hazırlanmıştır.
Algoritmaların çalışma mantığını anlamak için yorum satırları eklenmiştir.




Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları
Proje Amacı

Bu projede farklı arama ve sıralama algoritmalarının Python dili ile uygulanması, çalışma mantıklarının anlaşılması ve performanslarının karşılaştırılması amaçlanmıştır.

Arama Algoritmaları
Linear Search (Doğrusal Arama)
Listenin başından başlayarak tüm elemanları tek tek kontrol eder.
Sıralı olma şartı yoktur.
Zaman Karmaşıklığı: O(n)
Binary Search (İkili Arama)
Listeyi sürekli ikiye bölerek arama yapar.
Sadece sıralı listelerde çalışır.
Zaman Karmaşıklığı: O(log n)
Jump Search (Adımlamalı Arama)
Liste üzerinde belirli aralıklarla (√n) zıplayarak ilerler.
Uygun blok bulunduğunda doğrusal arama yapar.
Zaman Karmaşıklığı: O(√n)
Sıralama Algoritmaları
Bubble Sort
Komşu elemanları karşılaştırarak büyük olanı sağa iter.
Basit ama büyük verilerde yavaştır.
Zaman Karmaşıklığı: O(n²)
Selection Sort
Her adımda en küçük elemanı seçip başa yerleştirir.
Zaman Karmaşıklığı: O(n²)
Insertion Sort
Elemanları doğru konuma yerleştirerek sıralar.
Küçük veri setlerinde etkilidir.
Zaman Karmaşıklığı: O(n²)
Merge Sort
Böl ve fethet mantığıyla çalışır.
Listeyi parçalara ayırır ve sıralı şekilde birleştirir.
Zaman Karmaşıklığı: O(n log n)
Space Complexity: O(n)
Quick Sort
Pivot seçerek listeyi ikiye böler.
Ortalama durumda çok hızlıdır.
Zaman Karmaşıklığı: O(n log n)
Space Complexity: O(n)
Shell Sort
Insertion Sort’un geliştirilmiş halidir.
Belirli aralıklarla karşılaştırma yapar.
Zaman Karmaşıklığı: O(n log n) ile O(n²) arası
Algoritmaların Karşılaştırılması
Algoritma	Tür	Zaman Karmaşıklığı
Linear Search	Arama	O(n)
Binary Search	Arama	O(log n)
Jump Search	Arama	O(√n)
Bubble Sort	Sıralama	O(n²)
Selection Sort	Sıralama	O(n²)
Insertion Sort	Sıralama	O(n²)
Merge Sort	Sıralama	O(n log n)
Quick Sort	Sıralama	O(n log n)
Shell Sort	Sıralama	O(n log n) - O(n²)
Performans Analizi

Kod içerisinde time modülü kullanılarak her sıralama algoritmasının çalışma süresi ölçülmektedir.

Genel Sonuçlar
Basit algoritmalar (Bubble, Selection, Insertion) yavaştır.
Gelişmiş algoritmalar (Merge, Quick, Shell) daha hızlıdır.
Quick Sort ve Merge Sort genelde en iyi performansı verir.
Nasıl Çalıştırılır
Python yüklü olmalıdır
Dosyayı indir
Terminal veya VS Code’da çalıştır:
python dosya_adi.py

Örnek Çıktı
Orijinal liste ekrana yazdırılır
Sıralama algoritmaları çalışır
Arama algoritmaları sonuç döndürür
Performans karşılaştırması gösterilir
Not

Bu proje eğitim amaçlı hazırlanmıştır ve algoritmaların mantığını öğretmeyi hedefler.
