import math  # Matematiksel işlemler için (sqrt fonksiyonu)
import time  # Performans ölçümü için süre takibi

# ARAMA ALGORİTMALARI (SEARCHING ALGORITHMS)
# Arama algoritmaları, bir liste içinde belirli bir değeri bulmak için kullanılır.

def linear_search(arr, hedef):
    """
    LINEAR SEARCH (DOĞRUSAL ARAMA)
    - Çalışma Mantığı: Listenin en başından başlar, her elemanı tek tek hedefle kıyaslar.
    - Kullanım Alanı: Veri seti çok küçükse veya liste sıralı değilse kullanılır.
    - Zaman Karmaşıklığı: O(n) - Veri sayısı arttıkça süre doğrusal artar.
    """
    for i in range(len(arr)):       # Listenin her indeksini sırayla gez
        if arr[i] == hedef:         # Mevcut eleman hedefle eşleşiyor mu?
            return i                # Evet → indeksi döndür, aramayı bitir
    return -1                       # Tüm liste tarandı, eleman bulunamadı


def binary_search(arr, hedef):
    """
    BINARY SEARCH (İKİLİ ARAMA)
    - Çalışma Mantığı: Liste sürekli ikiye bölünür. Hedef ortadaki değerden küçükse sol,
      büyükse sağ tarafta arama devam eder.
    - ÖN ŞART: Liste mutlaka SIRALI olmalıdır.
    - Zaman Karmaşıklığı: O(log n) - Çok büyük verilerde inanılmaz hızlıdır.
    """
    dusuk = 0               # Arama aralığının başlangıç indeksi
    yuksek = len(arr) - 1   # Arama aralığının bitiş indeksi

    while dusuk <= yuksek:                  # Arama aralığı daraldıkça devam et
        orta = (dusuk + yuksek) // 2        # Tam ortadaki indeksi hesapla
        if arr[orta] == hedef:
            return orta                     # Hedef tam ortada → bulundu
        elif arr[orta] < hedef:
            dusuk = orta + 1                # Hedef sağ yarıda → sol sınırı ortanın sağına taşı
        else:
            yuksek = orta - 1              # Hedef sol yarıda → sağ sınırı ortanın soluna taşı
    return -1                              # Aralık sıfırlandı, eleman bulunamadı


def jump_search(arr, hedef):
    """
    JUMP SEARCH (ADIMLAMALI ARAMA)
    - Çalışma Mantığı: Belirli bir blok aralığında (genelde sqrt(n)) zıplayarak ilerler.
    - Hedefin olabileceği aralık bulunduğunda o aralıkta Linear Search yapar.
    - Zaman Karmaşıklığı: O(sqrt(n)) - Linear'den hızlı, Binary'den yavaştır.
    """
    n = len(arr)
    adim = int(math.sqrt(n))    # İdeal blok boyutu: listenin karekökü (örn. 100 elemanlı listede 10)
    onceki = 0                  # Bir önceki bloğun başlangıç noktası

    # Hedefin hangi blokta olduğunu bul: blok sonu hedeften küçük olduğu sürece zıpla
    while arr[min(adim, n) - 1] < hedef:
        onceki = adim               # Mevcut bloğu geç, bir sonrakine zıpla
        adim += int(math.sqrt(n))   # Adımı bir blok ilerlet
        if onceki >= n:
            return -1               # Liste bitti, eleman yok

    # Hedefin bulunduğu blokta doğrusal arama yap
    for i in range(onceki, min(adim, n)):
        if arr[i] == hedef:
            return i    # Eleman bulundu, indeksi döndür
    return -1           # Blokta bulunamadı


# SIRALAMA ALGORİTMALARI (SORTING ALGORITHMS)
# Sıralama algoritmaları, bir listeyi küçükten büyüğe düzenler.

def bubble_sort(arr):
    """
    BUBBLE SORT (KABARCIK) - O(n^2)
    Komşu elemanları kıyaslar ve büyük olanı sağa iter. Her döngüde en büyük
    eleman sağa 'kabarcık' gibi yerleşir. Basit ama yavaştır.
    """
    arr = arr.copy()    # Orijinal listeyi bozmamak için kopya al
    n = len(arr)
    for i in range(n):                      # Dış döngü: her turda bir eleman yerine oturur
        for j in range(0, n - i - 1):       # İç döngü: sona oturanları atlayarak karşılaştır
            if arr[j] > arr[j + 1]:         # Sol eleman sağdan büyükse yer değiştir (swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """
    SELECTION SORT (SEÇMELİ) - O(n^2)
    Her adımda listenin kalan kısmındaki en küçük elemanı bulur ve
    listenin başına (sıralanmamış kısmın başına) koyar.
    """
    arr = arr.copy()    # Orijinal listeyi bozmamak için kopya al
    for i in range(len(arr)):
        en_kucuk = i                            # Sıralanmamış kısmın başını en küçük say
        for j in range(i + 1, len(arr)):        # Geriye kalan elemanlarda daha küçüğü ara
            if arr[j] < arr[en_kucuk]:
                en_kucuk = j                    # Daha küçük bulundu, indeksi güncelle
        arr[i], arr[en_kucuk] = arr[en_kucuk], arr[i]  # En küçüğü başa taşı (swap)
    return arr


def insertion_sort(arr):
    """
    INSERTION SORT (ARAYA EKLEME) - O(n^2)
    Listenin başını sıralı kabul eder, yeni elemanı alıp sıralı kısmın
    içinde doğru yere 'insert' eder (sokar). Küçük listelerde verimlidir.
    """
    arr = arr.copy()    # Orijinal listeyi bozmamak için kopya al
    for i in range(1, len(arr)):        # İlk eleman zaten sıralı sayılır, 2.'den başla
        anahtar = arr[i]                # Yerleştirmek istediğimiz eleman
        j = i - 1                       # Sıralı kısmın son indeksi
        while j >= 0 and anahtar < arr[j]:  # Anahtar, solundakinden küçük olduğu sürece
            arr[j + 1] = arr[j]             # Soldaki elemanı bir sağa kaydır
            j -= 1                          # Bir adım daha sola git
        arr[j + 1] = anahtar            # Anahtarı doğru konumuna yerleştir
    return arr


def merge_sort(arr):
    """
    MERGE SORT (BİRLEŞTİRMELİ) - O(n log n)
    Listenin her bir elemanı tek kalana kadar böler, sonra bunları
    sıralı bir şekilde birleştirir. Kararlı ve hızlıdır.
    """
    arr = arr.copy()        # Orijinal listeyi bozmamak için kopya al
    if len(arr) > 1:        # Tek elemanlı liste zaten sıralıdır, bölmeye gerek yok
        orta = len(arr) // 2
        sol = merge_sort(arr[:orta])    # Sol yarıyı özyinelemeli (recursive) olarak sırala
        sag = merge_sort(arr[orta:])    # Sağ yarıyı özyinelemeli olarak sırala

        # Sıralı sol ve sağ yarıları birleştir
        i = j = k = 0   # i → sol indeks, j → sağ indeks, k → ana dizinin indeksi
        while i < len(sol) and j < len(sag):    # Her iki yarıda da eleman varken
            if sol[i] < sag[j]:
                arr[k] = sol[i]; i += 1         # Sol daha küçük → ana diziye al
            else:
                arr[k] = sag[j]; j += 1         # Sağ daha küçük → ana diziye al
            k += 1
        # Bir yarıda kalan elemanları olduğu gibi ekle
        while i < len(sol): arr[k] = sol[i]; i += 1; k += 1
        while j < len(sag): arr[k] = sag[j]; j += 1; k += 1
    return arr


def quick_sort(arr):
    """
    QUICK SORT (HIZLI) - Ortalamada O(n log n)
    Pivot seçer, küçükleri sol listeye, büyükleri sağa atar.
    Modern dillerin çoğunda standart sıralama algoritmasıdır.
    """
    if len(arr) <= 1:               # 0 veya 1 elemanlı liste zaten sıralıdır
        return arr
    pivot = arr[len(arr) // 2]      # Ortadaki elemanı pivot olarak seç
    sol   = [x for x in arr if x < pivot]   # Pivottan küçük olanlar sola
    orta  = [x for x in arr if x == pivot]  # Pivota eşit olanlar ortaya (tekrarlı sayılar için)
    sag   = [x for x in arr if x > pivot]   # Pivottan büyük olanlar sağa
    return quick_sort(sol) + orta + quick_sort(sag)  # Özyinelemeli sıralayıp birleştir


def shell_sort(arr):
    """
    SHELL SORT - O(n^2) ile O(n log n) arası
    Insertion Sort'un gelişmiş halidir. Elemanları belirli bir 'aralık' (gap)
    ile kıyaslayarak başlar ve bu aralığı her adımda küçültür.
    """
    arr = arr.copy()    # Orijinal listeyi bozmamak için kopya al
    n = len(arr)
    aralik = n // 2     # Başlangıç aralığı: listenin yarısı (örn. 10 elemanda aralik=5)

    while aralik > 0:                       # Aralık 0'a düşünce sıralama tamamdır
        for i in range(aralik, n):          # Aralık kadar ötedeki elemandan başla
            gecici = arr[i]                 # Yerleştireceğimiz elemanı sakla
            j = i
            while j >= aralik and arr[j - aralik] > gecici:  # Aralık kadar öndeki büyükse
                arr[j] = arr[j - aralik]    # O elemanı sağa kaydır
                j -= aralik                 # Bir aralık geri git
            arr[j] = gecici                 # Elemanı doğru konumuna yerleştir
        aralik //= 2    # Aralığı her turda yarıya indir, en son aralik=1 → klasik Insertion Sort
    return arr


# YARDIMCI FONKSİYON

def zaman_olc(fonksiyon, arr):
    """Verilen sıralama fonksiyonunun çalışma süresini saniye cinsinden ölçer."""
    basla = time.time()             # Başlangıç zamanını kaydet
    fonksiyon(arr.copy())           # Fonksiyonu çalıştır (.copy() ile orijinali koru)
    bitir = time.time()             # Bitiş zamanını kaydet
    return round(bitir - basla, 6)  # Geçen süreyi 6 ondalık basamakla döndür


# TEST VE SONUÇ EKRANI
# Bu blok sadece dosya doğrudan çalıştırıldığında çalışır.
# Başka bir dosyadan import edilirse çalışmaz.

if __name__ == "__main__":
    test_verisi = [64, 34, 25, 12, 22, 11, 90, 5, 45, 1]   # Test için örnek liste
    sirali = sorted(test_verisi)    # Arama testleri için sıralı versiyonu hazırla
    hedef = 22                      # Aranacak değer

    print(f"Orijinal Liste: {test_verisi}")
    print("-" * 40)

    # --- Sıralama Testleri ---
    # Her fonksiyona .copy() geçilmez çünkü fonksiyonların içinde zaten .copy() var
    print(f"1. Bubble Sort:    {bubble_sort(test_verisi)}")
    print(f"2. Selection Sort: {selection_sort(test_verisi)}")
    print(f"3. Insertion Sort: {insertion_sort(test_verisi)}")
    print(f"4. Merge Sort:     {merge_sort(test_verisi)}")
    print(f"5. Quick Sort:     {quick_sort(test_verisi)}")
    print(f"6. Shell Sort:     {shell_sort(test_verisi)}")

    # --- Arama Testleri ---
    print(f"\nArama Testi (Hedef: {hedef})")
    print(f"- Linear Search Indeksi : {linear_search(test_verisi, hedef)}  (sırasız listede)")
    print(f"- Binary Search Indeksi : {binary_search(sirali, hedef)}  (sirali listede)")
    print(f"- Jump Search Indeksi   : {jump_search(sirali, hedef)}  (sirali listede)")

    # --- Performans Karşılaştırması ---
    # Küçük listede farklar mikrosaniye düzeyindedir; büyük listede çok belirginleşir
    print("\nPerformans Karsilastirmasi:")
    print("-" * 40)
    for func in [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, shell_sort]:
        sure = zaman_olc(func, test_verisi)
        print(f"{func.__name__:20s}: {sure} saniye")