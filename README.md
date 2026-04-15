# veri-yapilari-odev-arama-siralama
Veri Yapıları Ve Algoritma dersi arama ve sıralama algoritmaları projesi
# Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları

# Proje Amacı
Bu projede farklı arama ve sıralama algoritmalarının Python dili ile uygulanması, çalışma mantıklarının anlaşılması ve performanslarının karşılaştırılması amaçlanmıştır.

# Arama Algoritmaları

# Linear Search (Doğrusal Arama)
- Listenin başından başlayarak tüm elemanları tek tek kontrol eder.
- Sıralı olma şartı yoktur.
- Zaman Karmaşıklığı: O(n)

# Binary Search (İkili Arama)
- Listeyi sürekli ikiye bölerek arama yapar.
- Sadece sıralı listelerde çalışır.
- Zaman Karmaşıklığı: O(log n)

# Jump Search (Adımlamalı Arama)
- Liste üzerinde belirli aralıklarla (√n) zıplayarak ilerler.
- Uygun aralık bulunduğunda doğrusal arama yapar.
- Zaman Karmaşıklığı: O(√n)

# Sıralama Algoritmaları

# Bubble Sort
- Komşu elemanları karşılaştırır ve büyük olanı sağa iter.
- Basit ama büyük verilerde yavaştır.
- Zaman Karmaşıklığı: O(n²)

# Selection Sort
- Her adımda en küçük elemanı seçip başa yerleştirir.
- Zaman Karmaşıklığı: O(n²)

# Insertion Sort
- Elemanları uygun konuma yerleştirerek sıralar.
- Küçük veri setlerinde etkilidir.
- Zaman Karmaşıklığı: O(n²)

# Merge Sort
- "Böl ve fethet" mantığıyla çalışır.
- Listeyi parçalara ayırır ve sıralı şekilde birleştirir.
- Zaman Karmaşıklığı: O(n log n)
- Space Complexity: O(n)

# Quick Sort
- Bir pivot seçerek listeyi ikiye böler.
- Ortalama durumda oldukça hızlıdır.
- Zaman Karmaşıklığı: O(n log n) (ortalama)
- Space Complexity: O(n)

# Shell Sort
- Insertion Sort’un geliştirilmiş halidir.
- Belirli aralıklarla karşılaştırma yapar.
- Zaman Karmaşıklığı: O(n log n) - O(n²)

# Algoritmaların Karşılaştırılması

| Algoritma       | Tür      | Zaman Karmaşıklığı |
|----------------|----------|-------------------|
| Linear Search  | Arama    | O(n)              |
| Binary Search  | Arama    | O(log n)          |
| Jump Search    | Arama    | O(√n)             |
| Bubble Sort    | Sıralama | O(n²)             |
| Selection Sort | Sıralama | O(n²)             |
| Insertion Sort | Sıralama | O(n²)             |
| Merge Sort     | Sıralama | O(n log n)        |
| Quick Sort     | Sıralama | O(n log n)        |
| Shell Sort     | Sıralama | O(n log n) - O(n²)|

# Performans Analizi

Kod içerisinde `time` modülü kullanılarak sıralama algoritmalarının çalışma süreleri ölçülmüştür.

Genel sonuç:
- Basit algoritmalar (Bubble, Selection, Insertion) büyük veri setlerinde daha yavaş çalışır.
- Gelişmiş algoritmalar (Merge, Quick, Shell) daha hızlı sonuç verir.
- Quick Sort ve Merge Sort genellikle en iyi performansı gösterir.

# Nasıl Çalıştırılır

1. Python yüklü olmalıdır.
2. Kod dosyasını bilgisayarınıza indirin.
3. Terminal veya VS Code üzerinden çalıştırın:

# Örnek Çıktı

Program çalıştırıldığında:
- Orijinal liste gösterilir
- Tüm sıralama algoritmalarının sonuçları yazdırılır
- Arama algoritmalarının indeks sonuçları gösterilir
- Performans karşılaştırması ekrana basılır

# Not

Bu proje eğitim amaçlı hazırlanmıştır.  
açıklayıcı yorum satırları eklenmiştir.

