Tugas 2:

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

Tugas 3:

Data delivery dibutuhkan agar informasi dapat berpindah secara aman dan konsisten serta dapat diproses dari satu komponen ke komponen yang lain dalam sebuah platform. Data delivery membantu menjaga akurasi data, sinkronisasi antar sistem, efisiensi dalam pertukaran efisiensi, serta memastikan format data seragam sehingga aplikasi bisa saling mengerti satu sama lain.

Menurut saya, JSON lebih baik daripada XML karena JSON memiliki format yang lebih mudah ditulis dan dibaca, mendukung penggunaan arrays, dan biasanya lebih mudah untuk diuraikan. Beberapa alasan yang sudah saya sebutkan adalah alasan-alasan paling utama mengapa JSON lebih populer dibandingkan XML untuk aplikasi modern.

Method is_valid() pada form Django berfungsi untuk memvalidasi apakah data yang dikirimkan melalui form sesuai berdasarkan definisi field dan constraint yang diberikan.

CSRF (Cross-Site Request Forgery) token digunakan untuk melindungi aplikasi dari serangan di mana penyerang mencoba memaksa pengguna yang sedang login untuk mengirim request berbahaya tanpa sepengetahuan pengguna tersebut. Apabila kita tidak menambahkan csrf_token, form akan menjadi rentan terhadap serangan CSRF karena penyerang dapat membuat halaman palsu yang mencoba mengirimkan request POST ke aplikasi dengan kredensial korban, mengingat cookie session korban masih aktif.

Untuk tutorial 2 kemarin, saya belum ada feedback untuk asisten dosen