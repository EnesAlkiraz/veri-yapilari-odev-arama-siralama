# Arama ve Sıralama Algoritmaları

Python ile geliştirilmiş, temel arama ve sıralama algoritmalarını bir arada sunan eğitim odaklı bir proje. Her algoritma; çalışma mantığı, zaman karmaşıklığı ve kullanım senaryoları açısından detaylıca açıklanmış ve yorumlanmıştır.

## Proje Hakkında

Bu proje, yazılım geliştirme süreçlerinde en sık kullanılan **3 arama** ve **6 sıralama** algoritmasını Python ile sıfırdan implement eder. Her fonksiyon satır satır Türkçe yorumlarla açıklanmış, `__main__` bloğu ise algoritmaların çıktı ve performanslarını karşılaştırmalı olarak gösterir.

**Kapsanan algoritmalar:**

| Kategori    | Algoritmalar |
|-------------|--------------|
| Arama       | Linear Search, Binary Search, Jump Search |
| Sıralama    | Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Shell Sort |

---

## Algoritmalara Genel Bakış

```
Girdi: [64, 34, 25, 12, 22, 11, 90, 5, 45, 1]

Bubble Sort    → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
Selection Sort → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
Insertion Sort → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
Merge Sort     → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
Quick Sort     → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
Shell Sort     → [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]

Hedef (22) için:
Linear Search  → index 4  (sırasız listede)
Binary Search  → index 4  (sıralı listede)
Jump Search    → index 4  (sıralı listede)
```

---

## Arama Algoritmaları

### 1. Linear Search (Doğrusal Arama)

Listenin en başından başlayarak her elemanı sırayla hedef değerle karşılaştırır. En basit arama yöntemidir.

```python
def linear_search(arr, hedef):
    for i in range(len(arr)):
        if arr[i] == hedef:
            return i
    return -1
```

**Ne zaman kullanılır?**
- Liste sırasız olduğunda
- Veri seti çok küçük olduğunda
- Tek seferlik bir arama yapılacağında

---

### 2. Binary Search (İkili Arama)

Her adımda arama aralığını yarıya böler. Ortadaki eleman hedeften küçükse sağa, büyükse sola odaklanır.

>  **Ön Şart:** Liste **mutlaka sıralı** olmalıdır.

```python
def binary_search(arr, hedef):
    dusuk, yuksek = 0, len(arr) - 1
    while dusuk <= yuksek:
        orta = (dusuk + yuksek) // 2
        if arr[orta] == hedef:
            return orta
        elif arr[orta] < hedef:
            dusuk = orta + 1
        else:
            yuksek = orta - 1
    return -1
```

**Ne zaman kullanılır?**
- Liste sıralı ve büyük olduğunda
- Tekrarlı aramalar yapılacağında

---

### 3. Jump Search (Adımlamalı Arama)

√n büyüklüğünde bloklar halinde ileri zıplayarak hedefin hangi blokta olduğunu bulur, ardından o blokta doğrusal arama yapar.

>  **Ön Şart:** Liste **sıralı** olmalıdır.

```python
def jump_search(arr, hedef):
    n = len(arr)
    adim = int(math.sqrt(n))
    # Blok bul, sonra doğrusal ara
```

**Ne zaman kullanılır?**
- Sıralı, büyük listelerde
- Binary Search'ten daha az karşılaştırma yapılmak istendiğinde (bazı sistemlerde)

---

## Sıralama Algoritmaları

### 1. Bubble Sort (Kabarcık Sıralama)

Komşu elemanları kıyaslayarak büyük olanı sağa doğru iter. Her turda en büyük eleman listenin sonuna "kabarcık" gibi yerleşir.

```python
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

**Özellikler:** Anlaşılması en kolay algoritmadır ancak büyük veri setlerinde yavaştır.

---

### 2. Selection Sort (Seçmeli Sıralama)

Her adımda sıralanmamış kısmın en küçük elemanını bulup listenin başına taşır.

```python
for i in range(len(arr)):
    en_kucuk = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[en_kucuk]:
            en_kucuk = j
    arr[i], arr[en_kucuk] = arr[en_kucuk], arr[i]
```

**Özellikler:** Her zaman tam olarak n(n-1)/2 karşılaştırma yapar. Takas sayısı azdır.

---

### 3. Insertion Sort (Araya Ekleme)

Listenin başını sıralı kabul eder, yeni her elemanı sıralı kısmın içindeki doğru konuma yerleştirir.

```python
for i in range(1, len(arr)):
    anahtar = arr[i]
    j = i - 1
    while j >= 0 and anahtar < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = anahtar
```

**Özellikler:** Küçük veya neredeyse sıralı listelerde çok verimlidir.

---

### 4. Merge Sort (Birleştirmeli Sıralama)

Böl-ve-fethet yaklaşımıyla çalışır: listeyi tek elemanlara kadar böler, sonra sıralı şekilde birleştirir.

```python
def merge_sort(arr):
    if len(arr) > 1:
        orta = len(arr) // 2
        sol = merge_sort(arr[:orta])
        sag = merge_sort(arr[orta:])
        # sol ve sag'ı birleştir
```

**Özellikler:** Kararlı (stable) bir algoritmadır. Büyük veri setlerinde güvenilir performans sunar. Ekstra bellek gerektirir.

---

### 5. Quick Sort (Hızlı Sıralama)

Bir pivot seçer; küçükleri sola, büyükleri sağa yerleştirir ve her iki yarıyı özyinelemeli olarak sıralar.

```python
def quick_sort(arr):
    pivot = arr[len(arr) // 2]
    sol   = [x for x in arr if x < pivot]
    orta  = [x for x in arr if x == pivot]
    sag   = [x for x in arr if x > pivot]
    return quick_sort(sol) + orta + quick_sort(sag)
```

**Özellikler:** Pratikte en hızlı algoritmalardan biridir. Python, Java, C++ gibi dillerin standart sort fonksiyonlarında kullanılır.

---

### 6. Shell Sort

Insertion Sort'un gelişmiş halidir. Başlangıçta büyük bir aralıkla karşılaştırma yapar ve aralığı giderek küçülterek klasik Insertion Sort'a dönüşür.

```python
aralik = n // 2
while aralik > 0:
    # aralik kadar uzaktaki elemanları insertion sort mantığıyla sırala
    aralik //= 2
```

**Özellikler:** Insertion Sort'tan belirgin şekilde hızlıdır. Ek bellek gerektirmez.

---

## Big-O Karmaşıklık Tablosu

| Algoritma      | En İyi    | Ortalama    | En Kötü     | Bellek  | Kararlı mı?|
|----------------|-----------|-------------|-------------|---------|-----------|
| Linear Search  | O(1)      | O(n)        | O(n)        | O(1)    | —         |
| Binary Search  | O(1)      | O(log n)    | O(log n)    | O(1)    | —         |
| Jump Search    | O(1)      | O(√n)       | O(√n)       | O(1)    | —         |
| Bubble Sort    | O(n)      | O(n²)       | O(n²)       | O(1)    |  Evet     |
| Selection Sort | O(n²)     | O(n²)       | O(n²)       | O(1)    |  Hayır    |
| Insertion Sort | O(n)      | O(n²)       | O(n²)       | O(1)    |  Evet     |
| Merge Sort     | O(n log n)| O(n log n)  | O(n log n)  | O(n)    |  Evet     |
| Quick Sort     | O(n log n)| O(n log n)  | O(n²)       | O(log n)|  Hayır    |
| Shell Sort     | O(n log n)| O(n log² n) | O(n²)       | O(1)    |  Hayır    |

> **Not:** Kararlı (stable) algoritma, eşit değerli elemanların orijinal sırasını korur.

---

## Algoritma Karşılaştırması

### Arama Algoritması Seçimi

```
Listem sıralı mı?
├─ Hayır → Linear Search
└─ Evet
   ├─ Küçük/orta boyut → Jump Search
   └─ Büyük boyut      → Binary Search  (en hızlı)
```

### Sıralama Algoritması Seçimi

```
Veri boyutu nedir?
├─ Küçük (< 20 eleman)
│  ├─ Neredeyse sıralı → Insertion Sort 
│  └─ Rastgele         → Selection Sort
├─ Orta (20–1000 eleman)
│  └─ Shell Sort veya Insertion Sort
└─ Büyük (1000+ eleman)
   ├─ Kararlılık gerekli → Merge Sort 
   └─ Genel amaç        → Quick Sort 
```

### Performans Özeti

| Durum | Önerilen Algoritma | Neden? |
|---|---|---|
| Küçük, sırasız liste | Linear Search | Basit, ek şart yok |
| Büyük, sıralı liste | Binary Search | O(log n) ile inanılmaz hız |
| Neredeyse sıralı liste | Insertion Sort | En iyi durumda O(n) |
| Büyük, genel amaçlı | Quick Sort | Ortalamada en hızlı |
| Kararlılık kritik | Merge Sort | Sabit O(n log n), kararlı |
| Bellek kısıtlıysa | Shell Sort | O(1) ekstra bellek |

---

## Nasıl Çalıştırılır

### Gereksinimler

- Python 3.x (standart kütüphaneler kullanılır, ek kurulum gerekmez)

### Çalıştırma

```bash
# Repoyu klonla
git clone https://github.com/kullanici-adi/repo-adi.git
cd repo-adi

# Dosyayı doğrudan çalıştır
python main.py
```

### Beklenen Çıktı

```
Orijinal Liste: [64, 34, 25, 12, 22, 11, 90, 5, 45, 1]
----------------------------------------
1. Bubble Sort:    [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
2. Selection Sort: [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
3. Insertion Sort: [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
4. Merge Sort:     [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
5. Quick Sort:     [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]
6. Shell Sort:     [1, 5, 11, 12, 22, 25, 34, 45, 64, 90]

Arama Testi (Hedef: 22)
- Linear Search Indeksi : 4  (sırasız listede)
- Binary Search Indeksi : 4  (sirali listede)
- Jump Search Indeksi   : 4  (sirali listede)

Performans Karsilastirmasi:
----------------------------------------
bubble_sort         : 0.000012 saniye
selection_sort      : 0.000008 saniye
insertion_sort      : 0.000005 saniye
merge_sort          : 0.000021 saniye
quick_sort          : 0.000009 saniye
shell_sort          : 0.000006 saniye
```

### Kendi Verinizle Test Etme

`main.py` dosyasındaki `test_verisi` ve `hedef` değişkenlerini değiştirerek farklı verilerle deneyebilirsiniz:

```python
test_verisi = [15, 3, 88, 42, 7, 99, 1, 56]  # kendi listeniz
hedef = 42                                     # aranacak değer
```

---

## Proje Yapısı

```
 proje/
└── main.py      # Tüm algoritmalar ve test kodu
```

---
Hazırlayan:
Enes ALKİRAZ Öğrenci No: 25019921033 Bartın Üniversitesi - Yapay Zeka Operatörlüğü

Bu proje eğitim amaçlı hazırlanmıştır.
