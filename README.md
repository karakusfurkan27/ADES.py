# Enerji Depolama ve Üretim Simülasyonu - README

## Proje Hakkında

Bu proje, yenilenebilir enerji kaynaklarından (güneş ve rüzgar) üretilen enerjinin depolanmasını ve tüketim talebine göre kullanımını simüle eden bir uygulamadır. Kullanıcı, güneş ışığı süresi, rüzgar hızı ve enerji talebi gibi parametreleri girerek, enerji üretimi, depolama ve tüketim verilerini görselleştirebilir. Ayrıca, enerji kesintisi simülasyonu da yapılabilir. Uygulama, enerji verimliliğini analiz etmek ve enerji üretim ile depolama süreçlerini takip etmek için çeşitli grafikler ve raporlar sunar.

## Kullanıcı Arayüzü

Uygulama, kullanıcıdan aşağıdaki bilgileri alır:

- **Günlük Güneş Işığı Süresi (saat)**: Güneş ışığı süresi, güneş enerjisinin üretileceği süreyi belirler.
- **Rüzgar Hızı (km/saat)**: Rüzgar enerjisi üretimi için gerekli olan rüzgar hızını belirtir.
- **Enerji Talebi (kWh)**: Kullanıcının tüketmek istediği enerji miktarını ifade eder.
- **Kesinti Simülasyonu**: Bu seçenek, enerji üretiminin kesildiği bir durumu simüle eder. Aktivasyon durumunda enerji üretimi sıfırlanır ve depolama devreye girer.

## Özellikler

- **Enerji Depolama Sistemi**: Bu sistem, belirli bir kapasiteye sahip bataryalarda enerji depolar. Enerji, üretilen fazla enerjiyi depolamak veya enerji talebini karşılamak için kullanılır.
- **Yenilenebilir Enerji Üretimi**: Güneş ve rüzgar enerjisi üretimi, güneş ışığı süresi ve rüzgar hızına dayalı olarak hesaplanır.
- **Verimlilik Hesaplama**: Depolanan enerjinin verimliliği, üretilen enerji ile karşılaştırılarak hesaplanır.
- **Kesinti Durumu**: Elektrik kesintisi simülasyonu yapılabilir ve enerji üretimi sıfırlanarak sadece depolama kullanılabilir.
- **Enerji Üretimi, Depolama ve Talep Grafikleri**: Üretilen enerji, depolanan enerji ve enerji talebi günlük olarak görselleştirilir.
- **Aylık Rapor**: Uygulama, aylık enerji tüketimi ve üretimi ile ilgili bir rapor sunar.
- **Günlük Log**: Kullanıcının her gün için enerji üretimi, talebi ve depolama verilerini takip etmesini sağlar.

## Kullanım

1. **Uygulama Başlatma**: Uygulamayı çalıştırarak, enerji üretimi ve depolama simülasyonlarını başlatabilirsiniz.
2. **Parametre Girişi**: Ekranda yer alan giriş kutularına günlük güneş ışığı süresi, rüzgar hızı ve enerji talebini girin.
3. **Simülasyon Başlatma**: "Simülasyonu Başlat" butonuna tıklayarak simülasyonu başlatın. Uygulama, enerji üretimini ve depolama sürecini simüle eder.
4. **Grafikleri İnceleme**: Uygulama, enerji üretimi, talebi ve depolama durumunu görsel olarak gösterecek bir grafik oluşturur.
5. **Kesinti Durumu**: Eğer kesinti simülasyonunu etkinleştirirseniz, enerji üretimi sıfırlanacak ve sadece depolama kullanılarak talep karşılanacaktır.
6. **Raporlar**: Aylık rapor ve günlük logları görüntüleyebilirsiniz. Aylık rapor, toplam tüketim ve üretim miktarlarını gösterir. Günlük log, her günün detaylı verilerini sağlar.

## Gereksinimler

- Python 3.x
- Aşağıdaki kütüphaneler:
  - `numpy`
  - `tkinter`
  - `matplotlib`

## Yükleme

Python ve gerekli kütüphaneleri yüklemek için aşağıdaki komutları terminalde çalıştırabilirsiniz:

```bash
pip install numpy matplotlib
```
