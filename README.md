<details>
<summary>Tugas Individu 2</summary>

Langkah-langkah yang saya lakukan untuk mengimplementasikan checklist di atas adalah:
1. Membuat dan mengaktifkan Virtual Environment beserta Dependencies nya.
2. Membuat proyek Django.
3. Mengkonfigurasikan Environment yang akan digunakan.
4. Membuat aplikasi main.
5. Membuat desain model Product dengan atribut wajib yang diberikan dan juga category_choices sendiri.
6. Mengaplikasikan migrasi model yang sudah dibuat.
7. Membuat views yang menampilkan informasi yang diminta soal.
8. Memasang Routing di file urls.
9. Melakukan Deployment ke PWS.

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
</details>

<details>
<summary>Tugas Individu 3</summary>

Data delivery dibutuhkan agar informasi dapat berpindah secara aman dan konsisten serta dapat diproses dari satu komponen ke komponen yang lain dalam sebuah platform. Data delivery membantu menjaga akurasi data, sinkronisasi antar sistem, efisiensi dalam pertukaran efisiensi, serta memastikan format data seragam sehingga aplikasi bisa saling mengerti satu sama lain.

Menurut saya, JSON lebih baik daripada XML karena JSON memiliki format yang lebih mudah ditulis dan dibaca, mendukung penggunaan arrays, dan biasanya lebih mudah untuk diuraikan. Beberapa alasan yang sudah saya sebutkan adalah alasan-alasan paling utama mengapa JSON lebih populer dibandingkan XML untuk aplikasi modern.

Method is_valid() pada form Django berfungsi untuk memvalidasi apakah data yang dikirimkan melalui form sesuai berdasarkan definisi field dan constraint yang diberikan.

CSRF (Cross-Site Request Forgery) token digunakan untuk melindungi aplikasi dari serangan di mana penyerang mencoba memaksa pengguna yang sedang login untuk mengirim request berbahaya tanpa sepengetahuan pengguna tersebut. Apabila kita tidak menambahkan csrf_token, form akan menjadi rentan terhadap serangan CSRF karena penyerang dapat membuat halaman palsu yang mencoba mengirimkan request POST ke aplikasi dengan kredensial korban, mengingat cookie session korban masih aktif.

Langkah-langkah yang saya lakukan untuk mengimplementasikan checklist di atas adalah:
1. Membuat berkas HTML bernama base.html yang berfungsi sebagai template dasar halaman web lainnya di dalam proyek.
2. Membuat form input data menggunakan Django modelform dan field yang sesuai dengan aplikasi saya
3. Membuat fungsi create_products dan show_products di views.py.
4. Membuat main.html dapat menambahkan produk serta memuat semua informasi produk yang sudah ditambahkan.
5. membuat dua berkas HTML baru sebagai halaman input dan juga detail produk.
6. buat fungsi show_xml, show_json, dan yang dengan menggunakan id di views.py.
7. import semua fungsi baru (create_products, show_products, show_...) ke urls.py dan masukkan ke urlpatterns
8. Gunakan Postman untuk mengecek pengiriman data.

Untuk tutorial 2 kemarin, saya belum ada feedback untuk asisten dosen

Show XML
<img width="1920" height="1200" alt="Screenshot 2025-09-16 214757" src="https://github.com/user-attachments/assets/fa9c0dce-0965-4af7-9c6d-0c1885d8c00e" />

Show JSON
<img width="1920" height="1200" alt="Screenshot 2025-09-16 214840" src="https://github.com/user-attachments/assets/a81f422c-c3ba-40ff-ac82-f479f1f134e7" />

Show XML by id
<img width="1920" height="1200" alt="Screenshot 2025-09-16 214814" src="https://github.com/user-attachments/assets/6fff1011-4a06-49be-bc20-e29c1d250712" />

Show JSON by id
<img width="1920" height="1200" alt="Screenshot 2025-09-16 214855" src="https://github.com/user-attachments/assets/755da7fe-b013-4143-a3c8-255047dce761" />
</details>

<details>
<summary>Tugas Individu 4</summary>

AuthenticationForm adalah form bawaan dari Django yang digunakan untuk melakukan autentikasi atau login. Form ini menyediakan field standar berupa username dan password yang dapat diperiksa kecocokannya dengan user yang terdaftar.

Kelebihan AuthenticationForm:
1. Siap pakai.
2. Terintegrasi dengan sistem Django.
3. Bisa di custom.

Kekurangan AuthenticationForm:
1. Field bawaan terbatas.
2. UI minimal.

Autentikasi adalah proses membuktikan identitas kita, sedangkan otorisasi adalah proses menentukan hak akses setelah identitas diketahui.
Django mengimplementasikan autentikasi dengan menyediakan mekanisme login atau logout.
Django mengimplementasikan otorisasi dengan menyediakan manajemen permissions seperti add dan delete.

Kelebihan cookies:
1. Tidak perlu disimpan di penyimpanan server.
2. Cocok untuk penyimpanan data kecil dan tidak sensitif seperti preferensi dalam tema dan bahasa.

Kekurangan cookies:
1. Ukuran yang terbatas.
2. Rentan terhadap penyerangan bila tidak dilindungi dengan baik.
3. Tidak cocok untuk penyimpanan data sensitif.

Kelebihan sessions:
1. Data disimpan di penyimpanan server sehingga lebih aman.
2. Cookie yang dikirim ke pengguna memiliki sensitifitas yang rendah.
3. Dapat menyimpan data yang lebih besar.

Kekurangan sessions:
1. Membebani penyimpanan server.
2. Perlu mekanisme tertentu agar session konsisten.
3. Lebih berbahaya ketika penyerang berhasil mencuri session id.

Tidak, cookies secara default tidak 100% aman, beberapa risiko yang akan dihadapi adalah serangan-serangan seperti XSS (Cross-Site Scripting), CSRF (Cross-Site Request Forgery), dan MitM (Man-in-the-Middle).
Django menangani risiko-risiko ini dengan menyediakan beberapa hal, di antaranya adalah CSRF middleware dan csrf_token yang mencegah request POST palsu, penggunaan HTTPS, dan menyimpan SECRET_KEY secara aman.

Langkah-langkah yang saya lakukan untuk mengimplementasikan checklist di atas adalah:
1. Membuat fungsi register, login, dan logout di views.py
2. Membuat page html untuk login dan register.
3. Import fungsi register, login, dan logout ke urls.py dan menambahkan pathnya ke urlspatterns.
4. Merestriksi akses halaman main pada pengguna yang belum login.
5. Menggunakan data dari cookies untuk menampilkan waktu terakhir login.
6. Menghubungkan model Product dengan User agar daftar produk dapat di filter berdasarkan user yang membuatnya.
</details>