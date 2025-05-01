# ARAÇ PLAKA TESPİT PROGRAMI
Proje Başlığı:
Araç Kapısı Plaka Tespit ve Kontrol Sistemi

Proje Amacı:
Bu projenin amacı, bir tesisin araç giriş noktasına yaklaşan araçların türünü (kamyon/tır veya diğer araçlar) ve plakalarını tespit ederek, duruma uygun şekilde fiziksel tepki verilmesini sağlamaktır. Geliştirilecek sistem, kamyon veya tır tespit edilip, plakası daha önceden sisteme kayıtlıysa Arduino üzerinden kapıyı açacaktır. Kamyon veya tır olmayan araçlar (örneğin otomobil) yaklaştığında ise sistem bir buzzer ile uyarı verecektir.

Teknoloji ve Platformlar:
Arayüz ve Uygulama: Flask tabanlı web uygulaması olarak geliştirilecektir. Uygulama, mobil cihazlarda çalışacak şekilde tasarlanacak olup, cep telefonlarının kamerası webcam olarak kullanılacaktır. Uygulama mobil çalıştırılamayan durumlarda, en azından bilgisayarda çalışır hale getirilmelidir.

Donanım: Arduino (kapı kontrolü ve buzzer uyarısı için kullanılacak)

Görüntü İşleme ve Derin Öğrenme: Araç ve plaka tespiti için YOLOv8 gibi bir derin öğrenme tabanlı nesne tanıma modeli kullanılacaktır.

OCR: Plaka üzerindeki yazıların okunması için EasyOCR veya Tesseract kütüphanelerinden biri tercih edilecektir.

Sistem Çalışma Prensibi:
Kamera görüntüsünden araç algılanır.

Araç tipi sınıflandırılır (Kamyon/Tır mı, değil mi).

Araç plakası okunur (OCR).

Plaka, sistemde önceden kayıtlı plakalarla karşılaştırılır.

Karara göre:

Kamyon/Tır + Kayıtlı plaka: Arduino ile kapı açılır.

Farklı araç türü veya kayıtsız plaka: Arduino üzerindeki buzzer aktif hale getirilerek uyarı verilir.

Arayüz Özellikleri:
Canlı Görüntü Sayfası:

Kamera görüntüsü gerçek zamanlı olarak gösterilecektir.

Kamyon veya tır algılandığında ekranda “Kamyon/Tır Tespit Edildi” uyarısı verilecektir.

Plaka tanımlandıktan sonra sistemde kayıtlıysa “Araç içeri alınıyor” mesajı gösterilecektir.

Plaka Yönetimi Sayfası:

Kullanıcılar, arayüz üzerinden sisteme yeni plakalar ekleyebilecek veya mevcut plakaları düzenleyebilecektir.

Veri Seti:
Kamyon/tır ve diğer araçlar olmak üzere iki farklı araç türüne ait 1000’er adet görüntü toplanacaktır.

Her bir görselde hem araçlar hem de plakalar bounding box ile etiketlenecektir.

Etiketleme işlemi Roboflow gibi bir platform kullanılarak yapılacaktır.

Test Süreci:
Uygulama, sahada çekilen yaklaşık 3 dakikalık bir video ile test edilecektir.

Videoda gerçek bir kamyonun görüntüsü ve plakası sistem tarafından algılanacak, plaka eşleşmesi doğrultusunda kapı açılacaktır.

Otomobil gibi farklı araçlar gösterildiğinde buzzer ile sesli uyarı verilecektir.

Teslimat ve Dokümantasyon:
Kodlar: GitHub üzerinde açık kaynak olarak paylaşılacaktır.

Veri Seti: Google Drive üzerinden ziplenmiş olarak paylaşılacaktır.

Raporlama: Proje raporu, model eğitimi, test sonuçları, sistem diyagramları ve kullanılan algoritmalar detaylı olarak içerecektir.


