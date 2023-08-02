# TA2
SISTEM PELACAK KAPAL 3GT – 30 GT MEMANFAATKAN KOMUNIKASI LORAWAN

![image](https://github.com/candramj/TA2/assets/44260141/0c6f37e9-6fda-4fb1-819e-fbbdbc7001f9)

Berikut gambaran umum sistem. Setiap kapal dinamakan node yang dipasang perangkat TTGO T-Beam. Perangkat TTGO T-Beam memanfaatkan modul GPS untuk mendapatkan data longitude dan latitude untuk mengetahui posisi kapal dan data tersebut dikirim ke Gateway menggunakan Lora. Gateway terdapat dua fungsi yaitu pertama sebagai penerima data dari Lora dan fungsi kedua sebagai pengirim data ke server menggunakan protocol MQTT. Bagian akhir dari sistem pemantau kapal ini adalah berupa website yang menampilkan informasi pelacakan kapal berupa peta dengan menampilkan posisi kapal secara real time.
