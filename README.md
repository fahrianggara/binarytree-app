<p align="center"><a href="https://bsi.ac.id" target="_blank"><img src="https://pbs.twimg.com/media/DpNiWO7UcAUQKEq.png" width="200"></a></p>

# Project Struktur Data

Project ini dibuat untuk memenuhi tugas mata kuliah Struktur Data. Dengan tema Aplikasi Pohon Biner. Yang akan diimplementasikan dalam bahasa pemrograman python. Untuk konversi ini dari Infix ke Postfix & Prefix. Menggunakan metode Stack.

## Cara Penggunaan

1. Clone repository ini
2. Buka terminal dan masuk ke direktori repository ini
3. Install Tabulate dengan perintah `pip install tabulate`
4. Jalankan perintah `py main.py`
5. Masukkan ekspresi infix. Contoh: `(A+(B*C))`
6. Dan sudah di konversi menjadi postfix dan prefix ditambah ada step by stepnya
7. Hasilnya akan seperti ini

```
Masukkan Notasi Infix (q untuk exit): (A+(B*C))

Hasil Konversi Infix => Postfix & Prefix:
+-----------+-----------+-----------+
| Infix     | Postfix   | Prefix    |
+-----------+-----------+-----------+
| (A+(B*C)) | A B C * + | + A * B C |
+-----------+-----------+-----------+

Step by Step Infix => Postfix:
+--------+-----------+--------+-----------+---------+
|   Step | Input     | Char   | Output    | Stack   |
+========+===========+========+===========+=========+
|      1 | (A+(B*C)) | (      |           | (       |
+--------+-----------+--------+-----------+---------+
|      2 | (A+(B*C)) | A      | A         | (       |
+--------+-----------+--------+-----------+---------+
|      3 | (A+(B*C)) | +      | A         | ( +     |
+--------+-----------+--------+-----------+---------+
|      4 | (A+(B*C)) | (      | A         | ( + (   |
+--------+-----------+--------+-----------+---------+
|      5 | (A+(B*C)) | B      | A B       | ( + (   |
+--------+-----------+--------+-----------+---------+
|      6 | (A+(B*C)) | *      | A B       | ( + ( * |
+--------+-----------+--------+-----------+---------+
|      7 | (A+(B*C)) | C      | A B C     | ( + ( * |
+--------+-----------+--------+-----------+---------+
|      8 | (A+(B*C)) | )      | A B C *   | ( +     |
+--------+-----------+--------+-----------+---------+
|      9 | (A+(B*C)) | )      | A B C * + |         |
+--------+-----------+--------+-----------+---------+
|     10 | (A+(B*C)) |        | A B C * + |         |
+--------+-----------+--------+-----------+---------+

Step by Step Infix => Prefix:
+--------+-----------+--------+-----------+---------+
|   Step | Input     | Char   | Output    | Stack   |
+========+===========+========+===========+=========+
|      1 | ((C*B)+A) | (      |           | (       |
+--------+-----------+--------+-----------+---------+
|      2 | ((C*B)+A) | (      |           | ( (     |
+--------+-----------+--------+-----------+---------+
|      3 | ((C*B)+A) | C      | C         | ( (     |
+--------+-----------+--------+-----------+---------+
|      4 | ((C*B)+A) | *      | C         | ( ( *   |
+--------+-----------+--------+-----------+---------+
|      5 | ((C*B)+A) | B      | C B       | ( ( *   |
+--------+-----------+--------+-----------+---------+
|      6 | ((C*B)+A) | )      | C B *     | (       |
+--------+-----------+--------+-----------+---------+
|      7 | ((C*B)+A) | +      | C B *     | ( +     |
+--------+-----------+--------+-----------+---------+
|      8 | ((C*B)+A) | A      | C B * A   | ( +     |
+--------+-----------+--------+-----------+---------+
|      9 | ((C*B)+A) | )      | C B * A + |         |
+--------+-----------+--------+-----------+---------+
|     10 | ((C*B)+A) |        | C B * A + |         |
+--------+-----------+--------+-----------+---------+
|     11 | ((C*B)+A) |        | + A * B C |         |
+--------+-----------+--------+-----------+---------+
```

## Anggota Kelompok

1. Fahri Anggara - 10220009
2. Dimas Yusuf Hidayat - 10220014
3. Fakhri Akmal Fadillah - 10220046
4. Sultan Jordy Priadi - 10220078
5. Ilham Ramadan - 10220048
