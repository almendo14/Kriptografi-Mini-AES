<<<<<<< HEAD
# Kriptografi Mini-AES 16-bit

## Deskripsi Proyek
Proyek ini adalah implementasi algoritma **Mini-AES** dengan panjang kunci 16-bit dan 3 ronde. Mini-AES adalah versi sederhana dari algoritma **AES** yang digunakan untuk mengenkripsi dan mendekripsi data dalam bentuk blok.

### Fitur
- Enkripsi dan dekripsi data dengan menggunakan algoritma Mini-AES.
- Menggunakan operasi dasar kriptografi seperti **SubNibbles**, **ShiftRows**, **MixColumns**, dan **AddRoundKey**.
- Proyek ini ditulis dalam bahasa pemrograman Python.



# Mini-AES 16-bit (3 Ronde)

Mini-AES 16-bit adalah varian dari algoritma AES yang menggunakan panjang kunci 16-bit dan menjalankan proses enkripsi dalam 3 ronde. Implementasi ini mencakup fungsi-fungsi dasar dari AES seperti **SubNibbles**, **ShiftRows**, **MixColumns**, dan **AddRoundKey**. 

## Deskripsi Kode

### 1. **S-Box (Substitution Box)**
S-Box digunakan untuk mengganti nilai byte dalam operasi SubNibbles. S-Box ini bersifat tetap dan telah didefinisikan sebagai berikut:

```python
SBOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}
=======
## Diagram Mini-AES

![Diagram Mini-AES](images/code%20kriptografi.jpg)
>>>>>>> 342bf5c (Menambahkan gambar ke README)
