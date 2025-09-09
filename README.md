Langkah-langkah yang saya lakukan untuk mengimplementasikan checklist di atas adalah:
1. Membuat dan mengaktifkan Virtual Environment beserta Dependencies nya.
2. Membuat proyek Django.
3. Mengkonfigurasikan Environment yang akan digunakan.
4. Membuat aplikasi main
5. Membuat desain model Product dengan atribut wajib yang diberikan dan juga category_choices sendiri
6. Mengaplikasikan migrasi model yang sudah dibuat
7. Membuat views yang menampilkan informasi yang diminta soal
8. Memasang Routing di file urls
9. Melakukan Deployment ke PWS

Berikut bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya
![alt text](https://tas-dp-prod-media.s3.amazonaws.com/blog/reqresp.jpg)

urls.py disini berperan terhadap URL ROUTER untuk memastikan kecocokan dengan request

views.py disini berperan dalam menyimpan logika utama untuk memproses request, memanggil model, dan mengirim konteks ke template

models.py disini berperan dalam mendefinisikan struktur data aplikasi dan digunakan oleh views.py ketika dibutuhkan

berkas html disini berperan dalam menerima konteks dari views.py untuk ditampilkan ke pengguna dalam bentuk UI

settings.py dalam proyek Django berperan sebagai tempat konfigurasi pusat proyek tersebut. File tersebut berisi pengaturan-pengaturan penting seperti daftar aplikasi yang digunakan dalam proyek tersebut, middleware yang aktif, hingga pengaturan keamanan seperti secret key.

Migrasi database di Django bekerja dengan mengubah skema DB agar sesuai model yang ada di dalam proyek. Django mula-mula membandingkan state model dengan hasil migrasi yang ada dan menciptakan file migrasi yang baru. Django kemudian mengeksekusi operasi migrasi tersebut ke database dan mencatat history migrasi tersebut.

Menurut saya, Django adalah framework yang sangat baik untuk digunakan sebagai permulaan pembelajaran pengembangan perangkat lunak karena Django menyediakan fitur built-in yang lengkap. Kemudian penggunaan bahasa python juga dapat membantu karena memiliki sintaks yang ramah pemula.

Untuk tutorial 1 kemarin, saya belum ada feedback untuk asisten dosen