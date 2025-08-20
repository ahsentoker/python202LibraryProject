# Global AI Hub Python 202 Bootcamp - Kütüphane Projesi

## Proje Hakkında

Bu proje, Python 202 Bootcamp kapsamında Nesne Yönelimli Programlama (OOP), harici API kullanımı ve FastAPI ile kendi API'nizi oluşturma konularını kapsayan üç aşamalı bir kütüphane yönetim uygulamasıdır.

### Aşamalar:

1. **OOP ile Terminalde Çalışan Kütüphane:**  
   Kitapların `Book` sınıfı ile tanımlandığı ve `Library` sınıfı ile yönetildiği, JSON dosyasına veri kaydeden ve okuyan terminal tabanlı uygulama.

2. **Harici API ile Veri Zenginleştirme:**  
   Kitap bilgileri kullanıcıdan manuel değil, ISBN numarası ile Open Library API’den çekilerek kütüphaneye eklenir.

3. **FastAPI ile Kendi API'nizi Oluşturma:**  
   Uygulama RESTful bir API haline getirilir. Kitap ekleme, listeleme ve silme işlemleri HTTP endpointleri üzerinden yapılabilir.

---

## Kurulum

1. Reponuzu klonlayın:

```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
```

2. Sanal ortam oluşturun ve aktif edin (opsiyonel ama önerilir):

   * Linux / MacOS:

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   * Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Gerekli paketleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

## Kullanım

### Aşama 1 ve 2: Terminal Uygulaması

```bash
python main.py
```

* Menüden seçim yaparak kitap ekleyebilir, silebilir, listeleyebilir ve ISBN ile kitap ekleyebilirsiniz.

### Aşama 3: FastAPI Sunucusu

```bash
uvicorn api:app --reload
```

* Sunucu çalıştıktan sonra tarayıcıdan [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) adresine giderek API dokümantasyonunu ve testlerini yapabilirsiniz.

## API Dokümantasyonu

* **GET /books**
  Tüm kitapların listesini JSON olarak döner.

* **GET /books/{isbn}**
  Belirtilen ISBN’e sahip kitabı döner.

* **POST /books**
  Request body'de sadece ISBN alanı içerir:

  ```json
  {
    "isbn": "978-0321765723"
  }
  ```

  Bu ISBN üzerinden Open Library API'den bilgi çekip, kütüphaneye yeni kitap ekler.

* **DELETE /books/{isbn}**
  Belirtilen ISBN’e sahip kitabı kütüphaneden siler.

## Testler

Testleri çalıştırmak için:

```bash
pytest
```

* `tests/` klasöründe hem terminal uygulaması hem API için test dosyaları bulunmaktadır.






