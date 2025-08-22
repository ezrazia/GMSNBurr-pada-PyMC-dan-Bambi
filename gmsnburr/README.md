# Petunjuk File untuk GMSNBurr

## [📦 Cek GPU](./cek_gpu.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_cek_gpu.py_](./cek_gpu.py)           |
| Isi File                 | File Python ini digunakan untuk mendeteksi dan menggunakan GPU sebelum melakukan komputasi.           |
| Tujuan                   | Jika ingin menggunakan GPU dalam komputasi, jalankan file ini terlebih dahulu sebelum menjalankan notebook atau kode utama. Jika GPU terdeteksi dan siap digunakan, proses komputasi akan menggunakan GPU.|
| Penggunaan    | 1. Unduh File<br>2. Jalankan File|

## [📦 Requirements](./requirements.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_requirements.py_](./requirements.py)           |
| Isi File                 | File Python ini berisikan package-package Python yang dibutuhkan ketika menggunakan PyMC dan Bambi.           |
| Dependensi                   | File Python ini dibutuhkan oleh _[gmsnburr_pymc.py](./gmsnburr_pymc.py)_ dan _[gmsnburr_bambi.py](./gmsnburr_bambi.py)_. Jika ingin menggunakan file tersebut, jalankan file ini terlebih dahulu.|
| Penggunaan    | 1. Unduh File<br>2. Jalankan File|

## [📦 GMSNBurr pada PyMC](./gmsnburr_pymc.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_gmsnburr_pymc.py_](./gmsnburr_pymc.py)           |
| Isi File                 | File Python ini berisikan kode program GMSNBurr pada PyMC.           |
| Tujuan                   | File Python ini digunakan jika pengguna hanya membutuhkan PyMC saja.|
| Penggunaan    | 1. Unduh File [_requirements.py_](./requirements.py) dan [_gmsnburr_pymc.py_](./gmsnburr_pymc.py) <br>2. Jalankan File [_requirements.py_](./requirements.py)<br>3. Jalankan File [_gmsnburr_pymc.py_](./gmsnburr_pymc.py) |

## [📦 GMSNBurr pada Bambi](./gmsnburr_bambi.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_gmsnburr_bambi.py_](./gmsnburr_bambi.py)           |
| Isi File                 | File Python ini berisikan kode program GMSNBurr pada Bambi.           |
| Tujuan                   | File Python ini merupakan struktur kode Bambi untuk distribusi GMSNBurr.|
| Penggunaan    | 1. Unduh File [_requirements.py_](./requirements.py), [_gmsnburr_pymc.py_](./gmsnburr_pymc.py), dan [_gmsnburr_bambi.py_](./gmsnburr_bambi.py) <br>2. Jalankan File [_requirements.py_](./requirements.py)<br>3. Jalankan File [_gmsnburr_pymc.py_](./gmsnburr_pymc.py)<br>4. Jalankan File [_gmsnburr_bambi.py_](./gmsnburr_bambi.py) |

## [📦 GMSNBurr](./gmsnburr.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_gmsnburr.py_](./gmsnburr.py)           |
| Isi File                 | File Python ini berisikan kode program GMSNBurr pada PyMC dan Bambi.           |
| Tujuan                   | File Python ini digunakan untuk seluruh kode program pada PyMC dan Bambi secara langsung tanpa perlu dependensi lain.|
| Penggunaan    | 1. Unduh File <br>2. Jalankan File|

## [📦 Implementasi dan Demonstrasi GMSNBurr](./gmsnburr_implement_demo.py)

| Deskripsi                | Detail |
|:--------------------------|:----------------|
| Nama File              | [_gmsnburr_implement_demo.py_](./gmsnburr_implement_demo.py.py)           |
| Isi File                 | File Python Notebook ini berisikan seluruh proses atau alur dari penambahan distribusi GMSNBurr pada PyMC dan Bambi hingga testing dan demonstrasi.           |
| Tujuan                   | File Python ini memberikan seluruh alur implementasi hingga demonstrasi. Demonstrasi juga dilakukan sesuai dengan alur kerja inferensi Bayesian yang bisa dijadikan pedoman.|
| Penggunaan    | 1. Unduh File<br>2. Jalankan File|
