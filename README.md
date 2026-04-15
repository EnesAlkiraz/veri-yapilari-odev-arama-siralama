# veri-yapilari-odev-arama-siralama
Veri Yapıları Ve Algoritma dersi arama ve sıralama algoritmaları projesi
# 🚀 Python Algoritma Rehberi: Arama ve Sıralama

Bu depo, bilgisayar bilimleri eğitiminde en çok karşımıza çıkan temel **Arama** ve **Sıralama** algoritmalarını derinlemesine incelemek ve performanslarını karşılaştırmak amacıyla oluşturulmuştur.

Kod içerisinde her fonksiyon; **zaman karmaşıklığı**, **çalışma prensibi** ve **ideal kullanım senaryoları** ile birlikte belgelenmiştir.

---

## 📂 Algoritma Detayları

### 1. Arama Algoritmaları (Searching Algorithms)
Veri yapıları içinde hedeflenen elemanın konumunu bulmaya yarayan yöntemlerdir.

| Algoritma | Zaman Karmaşıklığı (Best/Avg/Worst) | Özellik |
| :--- | :---: | :--- |
| **Linear Search** | $O(1) / O(n) / O(n)$ | Sıralama gerektirmez, küçük listelerde idealdir. |
| **Binary Search** | $O(1) / O(\log n) / O(\log n)$ | **Sıralı liste şarttır.** Çok hızlı sonuç verir. |
| **Jump Search** | $O(1) / O(\sqrt{n}) / O(\sqrt{n})$ | Binary ve Linear arasında bir orta yoldur. |

---

### 2. Sıralama Algoritmaları (Sorting Algorithms)
Düzensiz bir veri kümesini belirli bir kurala göre (sayısal veya alfabetik) dizen yöntemlerdir.

#### 🐢 Yavaş Algoritmalar ($O(n^2)$)
Genellikle eğitim amaçlı ve küçük veri setlerinde tercih edilirler:
* **Bubble Sort:** Komşu elemanları sürekli takas ederek en büyük elemanı sona iter.
* **Selection Sort:** Her turda listenin en küçüğünü "seçer" ve en başa koyar.
* **Insertion Sort:** Bir kart oyununda kağıtları dizmek gibi, her elemanı sıralı kısmın içine yerleştirir.

#### ⚡ Hızlı Algoritmalar ($O(n \log n)$)
Büyük veri setlerinde ve profesyonel yazılımlarda tercih edilen yöntemlerdir:
* **Merge Sort:** "Böl ve Yönet" prensibiyle çalışır. Listeyi tek eleman kalana kadar böler ve sıralayarak birleştirir.
* **Quick Sort:** Bir pivot noktası belirler ve elemanları bu pivottan küçük/büyük olmasına göre gruplandırır.
* **Shell Sort:** Insertion Sort'un uzak elemanları karşılaştırabilen daha verimli bir versiyonudur.

---

## 🛠️ Kurulum ve Çalıştırma

Kodun çalışması için standart Python kütüphanesi yeterlidir (herhangi bir dış kütüphane yüklemenize gerek yoktur).

1.  Depoyu klonlayın:
    ```bash
    git clone [https://github.com/kullaniciadin/proje-adin.git](https://github.com/kullaniciadin/proje-adin.git)
    ```
2.  Dosyayı çalıştırın:
    ```bash
    python main.py
    ```

---

## 📊 Performans Analizi

Kod içerisindeki `zaman_olc` fonksiyonu, algoritmaların gerçek dünya performansını ölçer. 

> **Not:** $O(n^2)$ olan algoritmalar (Bubble, Selection) veri seti büyüdükçe (örneğin 10.000 eleman) dramatik bir şekilde yavaşlarken; $O(n \log n)$ olanlar (Quick, Merge) saniyeler içinde işlemi tamamlar.
