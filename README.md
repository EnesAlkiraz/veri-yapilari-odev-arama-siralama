# Arama ve Sıralama Algoritmaları – Python Uygulaması

## Genel Bakış
Bu proje, temel arama ve sıralama algoritmalarının Python ile uygulanmasını ve çalışma mantıklarının anlaşılmasını amaçlamaktadır. Ayrıca farklı algoritmaların performans farklarını gözlemlemek için basit bir karşılaştırma mekanizması içerir.

Kod içerisinde hem klasik yöntemler hem de daha optimize yaklaşımlar birlikte ele alınmıştır.
## İçerik

### Arama Algoritmaları
- Linear Search (Doğrusal Arama)
- Binary Search (İkili Arama)
- Jump Search (Atlamalı Arama)

### Sıralama Algoritmaları
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Shell Sort

## Arama Algoritmaları

### Linear Search
Liste baştan sona kadar taranarak her eleman hedef değer ile karşılaştırılır.
- Sıralama gerektirmez
- Küçük veri setlerinde kullanılabilir
- Zaman karmaşıklığı: O(n)

### Binary Search
Sıralı bir liste üzerinde çalışır ve arama alanını her adımda ikiye böler.
- Sadece sıralı listelerde çalışır
- Büyük veri setlerinde oldukça hızlıdır
- Zaman karmaşıklığı: O(log n)

### Jump Search
Liste belirli bloklara bölünerek ilerlenir. Blok içinde doğrusal arama yapılır.
- Sıralı veri gerektirir
- Blok boyutu genellikle √n olarak seçilir
- Zaman karmaşıklığı: O(√n)

## Sıralama Algoritmaları

### Bubble Sort
Komşu elemanlar karşılaştırılarak büyük olanlar sağa doğru kaydırılır.
- Basit yapılıdır
- Büyük veri setlerinde verimsizdir
- Zaman karmaşıklığı: O(n²)

### Selection Sort
Her turda en küçük eleman bulunur ve doğru konumuna yerleştirilir.
- Swap sayısı azdır
- Performans olarak düşüktür
- Zaman karmaşıklığı: O(n²)

### Insertion Sort
Liste sıralı ve sırasız olmak üzere iki parçaya ayrılır. Yeni eleman doğru yere yerleştirilir.
- Küçük veya kısmen sıralı verilerde etkilidir
- Zaman karmaşıklığı: O(n²)

### Merge Sort
Liste sürekli ikiye bölünür ve sıralı şekilde birleştirilir.
- Böl ve yönet (divide & conquer) mantığı kullanır
- Stabil ve güvenilir bir algoritmadır
- Zaman karmaşıklığı: O(n log n)

### Quick Sort
Bir pivot seçilerek liste küçük ve büyük olmak üzere ikiye ayrılır.
- Pratikte en hızlı algoritmalardan biridir
- Ortalama performans: O(n log n)
- En kötü durumda: O(n²)

### Shell Sort
Insertion sort’un geliştirilmiş halidir. Belirli aralıklarla (gap) karşılaştırma yapar.
- Gap değeri zamanla azaltılır
- Orta seviyede performans sunar
- Zaman karmaşıklığı değişkendir

## Performans Ölçümü:
Sıralama algoritmalarının çalışma süresi `time` modülü kullanılarak ölçülmektedir.
Kodda kullanılan mantık:

```python
def zaman_olc(fonksiyon, arr):
    basla = time.time()
    fonksiyon(arr.copy())
    bitir = time.time()
    return round(bitir - basla, 6)

[64, 34, 25, 12, 22, 11, 90, 5, 45, 1]

python main.py
---
### 👨‍💻 Hazırlayan
**Enes ALKİRAZ** 🆔 Öğrenci No: **25019921033** 🏫 Bartın Üniversitesi - Yapay Zeka Operatörlüğü
Veri Yapıları Ve Algoritma dersi arama ve sıralama algoritmaları projesi

