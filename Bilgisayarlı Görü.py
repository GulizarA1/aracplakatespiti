# YOLOv8 modelini yükle (kamyon/tır için)
model = YOLO("yolov8n.pt")  # COCO sınıflarını içeriyor (class 7 = truck, class 2 = car)

# Plaka tanımak için OCR modeli
ocr_reader = easyocr.Reader(['en'])

# Yetkili plakalar (buraya dilediğin plakaları ekleyebilirsin)
authorized_plates = ["34ABC123", "06XYZ789"]

# Kamera akışı için
camera = cv2.VideoCapture(0)  # veya video dosyasıyla test için cv2.VideoCapture("video.mp4")

# Plaka veritabanına ekleme
@app.route("/add_plate", methods=['GET', 'POST'])
def add_plate():
    if request.method == 'POST':
        plate = request.form['plate'].upper()
        if plate not in authorized_plates:
            authorized_plates.append(plate)
        return redirect("/")
    return '''
        <form method="post">
            Yeni Plaka: <input name="plate">
            <input type="submit">
        </form>
    '''

# Araç tespit ve plaka tanıma işlemi

def gen():
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame)
        classes = results[0].boxes.cls.cpu().numpy()
        labels = [model.model.names[int(cls)] for cls in classes]

        truck_detected = any(label == "truck" for label in labels)
        car_detected = any(label == "car" for label in labels)

        message = "Araç bekleniyor..."
        buzzer = False
        gate_open = False

        if truck_detected:
            message = "Kamyon tespit edildi. Plaka okunuyor..."

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            results = ocr_reader.readtext(gray)

            for (bbox, text, prob) in results:
                text = text.replace(" ", "").upper()
                if len(text) >= 7:
                    if text in authorized_plates:
                        message = f"Plaka: {text} - Yetkili, kapı açılıyor!"
                        gate_open = True
                    else:
                        message = f"Plaka: {text} - Yetkisiz, erişim yok!"

        elif car_detected:
            message = "Otomobil tespit edildi. Buzzer uyarısı!"
            buzzer = True

        # Uyarı mesajı
        cv2.putText(frame, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Görüntüyü encode et
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Canlı video yayını
@app.route('/video')
def video():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Ana sayfa
@app.route('/')
def index():
    return '''
    <h1>Plaka Tespit Sistemi</h1>
    <img src="/video">
    <p><a href="/add_plate">Plaka Ekle</a></p>
    '''

# Uygulamayı başlat
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)