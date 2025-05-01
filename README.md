# 🚛 Araç Kapısı Plaka Tespit ve Kontrol Sistemi

Bu proje, araçların tesis girişine yaklaştığında türünü (kamyon/tır veya diğer) ve plakasını algılayarak uygun fiziksel aksiyonları (kapı açma veya buzzer ile uyarı) gerçekleştiren bir akıllı güvenlik sistemidir. Uygulama, Flask tabanlı bir web arayüzüyle mobil veya masaüstü cihazlarda çalışacak şekilde tasarlanmıştır.

## 🔧 Proje Özeti

- Kamyon/tır algılandığında ve plakası veritabanında varsa: **Arduino ile kapı açılır.**
- Kamyon/tır olmayan araç algılandığında: **Arduino üzerindeki buzzer çalışır.**
- Plaka tanıma işlemi OCR (Optical Character Recognition) ile gerçekleştirilir.
- Arayüzde canlı kamera görüntüsü, uyarılar ve plaka yönetimi ekranları bulunmaktadır.

## 🚀 Teknolojiler

- **Flask** – Web uygulaması geliştirme
- **OpenCV** – Görüntü işleme
- **YOLOv8 / CNN** – Nesne tespiti (araç ve plaka)
- **EasyOCR / Tesseract** – Plaka yazısı okuma
- **Arduino** – Fiziksel donanım kontrolü (kapı ve buzzer)
- **HTML/CSS + JavaScript** – Arayüz
- **SQLite / JSON** – Basit plaka veritabanı

## 📁 Proje Yapısı

📦 **vehicle-gate-detection**  
├── `app.py`  # Flask uygulaması  
├── `templates/`  # HTML dosyaları  
│   ├── `index.html`  # Ana arayüz (kamera, uyarılar)  
│   └── `register_plate.html`  # Plaka ekleme sayfası  
├── `static/`  # CSS / JS dosyaları  
├── `model/`  # Eğitilmiş YOLO veya CNN modeli  
├── `utils/`  # Yardımcı fonksiyonlar  
│   ├── `detection.py`  # Araç ve plaka tespiti  
│   ├── `ocr.py`  # OCR işlemleri  
│   └── `arduino_control.py`  # Arduino ile iletişim  
├── `dataset/`  # Görüntü veri seti (Drive linki)  
├── `README.md`  
└── `requirements.txt`  # Gerekli kütüphaneler

## 📸 Veri Seti

- **Kamyon/Tır Görselleri:** 1000 adet  
- **Diğer Araç Görselleri:** 1000 adet  
- **Etiketleme:** Bounding box ile hem araç hem plaka bölgeleri Roboflow üzerinden etiketlenmiştir.  
- **Veri Erişimi:** [Google Drive – ZIP Dosyası](#) ← (Bağlantıyı buraya ekleyin)

## 🧠 Model Eğitimi

### Katmanlar:

- `Convolution Layer`: Görüntüden öznitelik çıkarımı
- `MaxPooling`: Boyut küçültme ve gürültü azaltma
- `Fully Connected (Dense) Layer`: Karar mekanizması
- `ReLU`: Aktivasyon fonksiyonu
- `Sigmoid/Softmax`: Çıktı katmanı – sınıflandırma

### Öğrenme Süreci:

1. **Forward Propagation:** Girdi verisi katmanlardan geçerek çıktı üretir.
2. **Loss Calculation:** Üretilen tahmin ile gerçek değer arasındaki hata hesaplanır.
3. **Backpropagation:** Hata değeri geriye yayılır, her katmandaki ağırlıklar güncellenir.
4. **Optimization (Gradient Descent):** Ağırlıklar, hatayı minimize edecek şekilde yeniden ayarlanır.

Model, `YOLOv8` ya da özelleştirilmiş `CNN` yapısı ile Google Colab üzerinde eğitilecektir.

## 🖥️ Arayüz Özellikleri

- **Kamera Görüntüsü:** Canlı olarak kameradan alınır.
- **Uyarılar:** Araç tipi ve plaka durumu ekranda gösterilir.
- **Plaka Kayıt Sayfası:** Yeni plakalar sisteme kaydedilebilir.

## 🔬 Test Süreci

- Sahadan çekilen 3 dakikalık gerçek video ile test yapılacaktır.
- Kamyon tespiti + kayıtlı plaka → Arduino kapıyı açar.
- Otomobil tespiti → Buzzer sesli uyarı verir.

## ⚙️ Arduino Entegrasyonu

- **Serial iletişim** (PySerial)
- **Kapı açma komutu** → `arduino.write(b'OPEN')`
- **Buzzer uyarı komutu** → `arduino.write(b'BUZZ')`

## 📝 Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

```bash
git clone https://github.com/kullaniciadi/vehicle-gate-detection.git
cd vehicle-gate-detection
pip install -r requirements.txt
python app.py
