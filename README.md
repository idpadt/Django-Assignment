Tugas 2 -------------------------------------------------------------------------------------------------------
1. Kaitan antara urls.py, views.py, models.py, and html?
Urls.py digunakan untuk merouting fungsi2 yang ada pada views.py
Views.py berfungsi menerima request dan mengembalikan respon menggunakan data yang ada pada models.py dan dalam bentuk html
Models.py berisi bentuk2 dari data yang ingin disimpan
Html merupakan respon yang akhirnya akan ditampilkan di browser

2. Why use virtual environment? What if we dont?
Karena proyek2 yang kita buat belum tentu memakai keperluan/requirements yang berbeda2, menggunakan virtual environment berarti mengisolasikan proyek yang ingin kita buat dengan settingan sistem yang kita pakai atau proyek lain sehingga tidak menimbulkan konflik antar proyek.

Jika kita tidak memakai venv, maka konflik antar proyek dapat muncul. Lalu setiap perubahan requirement akan mempengaruhi semua proyek sekaligus. Tak hanya itu, menyiapkan requirement, library, dependency, dll (ie environment/lingkungannya) akan menjadi sangat sulit.

3. Jelasin cara implementasi poin 1-4
1: pakai perintah "python manage.py startapp study_tracker"
2: menambah study_tracker.urls ke urlpatterns di urls.py dalam django_project
3: menambah class Assignment ke dalam models.py, lalu jalankan makemigrations lalu migrate
4: menambah fungsi show_tracker ke views.py yang sudah dirouting di study_tracker.urls yang akan memakai data dari models.py dan template dari tracker.html


Tugas 3 -------------------------------------------------------------------------------------------------------
1. Ada cara lain selain pakai forms? kelebihan pakai forms?
Yes, yakni pakai request POST data mentah. Namun memakai forms lebih mudah dipakai, divalidasi, dihandle, dan lebih aman.

2. Perbedaan antara JSON, XML, HTML?
Singkatnya, JSON lebih simple, ringah dan mudah dibaca/dimengerti, XML lebih lengkap dan lebih menyeluruh, sedangkan html lebih dipakai untuk penampilan situs web.

3. Knp perlu data delivery?
Antara lain adalah untuk lebih mudah dan lebih efisien dalam komunikasi antar bagian2 yang berbeda dalam platfrom, membantu memfasilitasi sambungan ke bagian external, dan juga membantu menjaga konsistensi.

4. Jelasin cara implementasi semua checklist
1: membuah fungsi AssignmentRecordForm dalam forms.py berdasarkan model Assignment dan dengan field nama, subjek, progres, dan deskripsi
2: menambah fungsi create_assignment di views.py yang sudah dirouting ke /create di urls.py yang akan membuat form berdasarkan forms.py yang sudah dibuat
3: menambah create_assignment.html yang akan menampilkan formnya
4: mengubah tracker.html dengan membuat tombol "Tambah Tugas" yang akan redirect ke /create
5: menambah show_xml dan show_json ke views.py yang akan mengambil semua data dan memberi respon yakni data tersebut dalam bentuk xml dan json
6: menambah /xml untuk show_xml dan /json untuk show_json ke dalam urls.py

Tugas 4 -------------------------------------------------------------------------------------------------------
1. "{% csrf_token %}" usage? Jika gaada?
Potongan kode tsb digunakan untuk melindungi form tsb dari serangan CSRF, yaitu serangan dimana situs atau aplikasi menipu browser untuk mengautentikasi tanpa izin. Jika gaada, maka form tsb akan menjadi lemah terhadap serangan CSRF.

2. Buat elemen form manual? Gimana caranya?
Yes you can. Caranya mirip seperti membuat form biasa, misalnya seperti form "Tugas Baru". Kebanding membuat field-fieldnya saja di forms.py dan tinggal form.as_table, kita perlu membuat manual setiap field. Pertama buat fungsi formnya yang mana harus menuliskan semua tipe field2nya, lalu di file html perlu memasukkan semua field secara manual.

3. Jelaskan alur masukin data ke HTML form, data ke database, lalu muncul data di HTML template
Pertama user memasukkan data melalui form, lalu data2 itu akan dipakai untuk membuat instance baru dari model yang dipakai, yang mana data model itu dapat dipakai untuk ditampilkan ke html lagi.

4. Jelasin cara implementasi semua checklist
1: Pertama buat fungsi register di views.py, lalu buat register.html untuk templatenya, lalu dirouting di urls.py, jika selesai register akan kembali ke halaman login
2: Sama seperti fitur register namun buat login, jika selesai login akan masuk ke halaman utama study_tracker
3: Pertama buat fungsi logout di views.py, lalu masukkan tombol logout di template utama study_tracker, lalu routing di urls.py, jika berhasil logout akan kembali ke halaman login
4: Tambah "@login_required(login_url='/tracker/login/')" diatas halaman study_tracker agak hanya bisa diakses jika sudah login

