<p align="center"><a href="https://bsi.ac.id" target="_blank"><img src="https://pbs.twimg.com/media/DpNiWO7UcAUQKEq.png" width="200"></a></p>

# Project Struktur Data

Project ini dibuat untuk memenuhi tugas mata kuliah Struktur Data. Dengan tema Aplikasi Pohon Biner. Yang akan diimplementasikan dalam bahasa pemrograman python. Untuk konversi ini dari Infix ke Postfix & Prefix. Menggunakan metode Stack.

## Cara Penggunaan

1. Clone repository ini
2. Buka terminal dan masuk ke direktori repository ini
3. Jalankan perintah `py main.py`
4. Masukkan ekspresi infix. Contoh: `(A+(B*C))`
5. Dan sudah di konversi menjadi postfix dan prefix ditambah ada step by stepnya
6. Hasilnya akan seperti ini

```
Masukkan Notasi Infix (q untuk exit): (A+(B*C))

Hasil Konversi Infix => Postfix & Prefix:
+-----------+---------+--------+
| Infix     | Postfix | Prefix |
+-----------+---------+--------+
| (A+(B*C)) | ABC*+   | +A*BC  |
+-----------+---------+--------+

Step by step Infix => Postfix:
+-----+-----------+----------+----------+---------+
|   # | Input     | Symbol   | Output   | Stack   |
+=====+===========+==========+==========+=========+
|   1 | (A+(B*C)) | (        |          | (       |
+-----+-----------+----------+----------+---------+
|   2 | (A+(B*C)) | A        | A        | (       |
+-----+-----------+----------+----------+---------+
|   3 | (A+(B*C)) | +        | A        | (+      |
+-----+-----------+----------+----------+---------+
|   4 | (A+(B*C)) | (        | A        | (+(     |
+-----+-----------+----------+----------+---------+
|   5 | (A+(B*C)) | B        | AB       | (+(     |
+-----+-----------+----------+----------+---------+
|   6 | (A+(B*C)) | *        | AB       | (+(*    |
+-----+-----------+----------+----------+---------+
|   7 | (A+(B*C)) | C        | ABC      | (+(*    |
+-----+-----------+----------+----------+---------+
|   8 | (A+(B*C)) | )        | ABC*     | (+      |
+-----+-----------+----------+----------+---------+
|   9 | (A+(B*C)) | )        | ABC*+    |         |
+-----+-----------+----------+----------+---------+

Step by step Infix => Prefix:
+----+-----------+----------+----------+---------+
|    | Input     | Symbol   | Output   | Stack   |
+====+===========+==========+==========+=========+
|  1 | ((C*B)+A) | (        |          | (       |
+----+-----------+----------+----------+---------+
|  2 | ((C*B)+A) | (        |          | ((      |
+----+-----------+----------+----------+---------+
|  3 | ((C*B)+A) | C        | C        | ((      |
+----+-----------+----------+----------+---------+
|  4 | ((C*B)+A) | *        | C        | ((*     |
+----+-----------+----------+----------+---------+
|  5 | ((C*B)+A) | B        | CB       | ((*     |
+----+-----------+----------+----------+---------+
|  6 | ((C*B)+A) | )        | CB*      | (       |
+----+-----------+----------+----------+---------+
|  7 | ((C*B)+A) | +        | CB*      | (+      |
+----+-----------+----------+----------+---------+
|  8 | ((C*B)+A) | A        | CB*A     | (+      |
+----+-----------+----------+----------+---------+
|  9 | ((C*B)+A) | )        | CB*A+    |         |
+----+-----------+----------+----------+---------+
```

## Anggota Kelompok

1. Fahri Anggara - 10220009
2. Dimas Yusuf Hidayat - 10220014
3. Fakhri Akmal Fadillah - 10220046
4. Sultan Jordy Priadi - 10220078
5. Ilham Ramadan - 10220048
