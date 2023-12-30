from modules.cyk import is_accepted

def test_atributif_adjektiva():
    assert is_accepted("Sepatu usang dibakar ayah") == True
    assert is_accepted("Ibu membeli baju mahal") == True
    assert is_accepted("Saya memiliki rumah sederhana") == True
    assert is_accepted("Anjing kecil menggigit baju") == True
    assert is_accepted("Naya makan makanan sehat") == True
    assert is_accepted("Mobil merah dicuci paman") == True
    assert is_accepted("Dia mencium mawar harum") == True
    assert is_accepted("Kakak menyukai barang mewah") == True
    assert is_accepted("Gitar tua dibeli kolektor") == True
    assert is_accepted("Kucing putih memainkan bola di taman") == True
    assert is_accepted("Hutan ditumbuhi pohon besar") == True
    assert is_accepted("Buku sastra klasik mengandung nilai estetika") == True
    assert is_accepted("Ikan segar ditangkap nelayan di laut") == True
    assert is_accepted("Kado spesial dibuat pacar dengan sepenuh hati") == True
    assert is_accepted("Teknologi canggih sudah digunakan manusia sehari-hari") == True
    assert is_accepted("Kayu lapuk dipotong tukang") == True
    assert is_accepted("Makanan pedas menggugah selera") == True
    assert is_accepted("Pemandangan indah menenangkan hati") == True
    assert is_accepted("Ia memiliki sepatu nyaman untuk dipakai") == True
    assert is_accepted("Nenek membuat teh panas") == True
    assert is_accepted("Olahraga membuat tubuh saya kuat") == True
    assert is_accepted("Kucing hitam membawa keberuntungan") == True
    assert is_accepted("Debu kotor menyelimuti kamar") == True
    assert is_accepted("Ayah memotong rumput kuning dengan mesin") == True


def test_predikatif_adjektiva():
    assert is_accepted("Rumah baru itu sangat besar") == True
    assert is_accepted("Lapangan bola itu luas") == True
    assert is_accepted("Tas ini sangat mahal") == True
    assert is_accepted("Sepatu anak itu sangat kecil") == True
    assert is_accepted("Berita itu sungguh menyedihkan") == True
    assert is_accepted("Baju baru itu bagus") == True
    assert is_accepted("Hati dia gundah") == True
    assert is_accepted("Penampilan mereka keren") == True
    assert is_accepted("Buku guru kami tebal") == True
    assert is_accepted("Kue itu enak") == True
    assert is_accepted("Mobil itu mewah") == True
    assert is_accepted("Solusi saya sederhana") == True
    assert is_accepted("Cerita beliau sedih") == True
    assert is_accepted("Ibu beli ikan segar") == True
    assert is_accepted("Budi mengecat tembok biru") == True
    assert is_accepted("Kabar itu membuat mereka bahagia") == True
    assert is_accepted("Roy membeli mawar merah") == True
    assert is_accepted("Saya merasa ide itu menarik") == True
    assert is_accepted("Dia menganggap tugas itu susah") == True
    assert is_accepted("Mereka memiliki ruangan nyaman") == True
    assert is_accepted("Kami mengecat atap ungu") == True
    assert is_accepted("Kami merasa film itu membosankan") == True
    assert is_accepted("Saya merasa buku ini menarik") == True
    assert is_accepted("Kami merasa suasana itu menenangkan") == True
    assert is_accepted("Dia merasa ujian itu menantang") == True


def test_keterangan_adjektiva():
    assert is_accepted("Diva mengerjakan secepatnya") == True
    assert is_accepted("Ryan menyanyi lagu bagus") == True
    assert is_accepted("Polisi menangkap penjahat dengan sekerasnya") == True
    assert is_accepted("Celia melewati jembatan sulit dengan takut") == True
    assert is_accepted("Perawat puskesmas menyambut pasien dengan lembut") == True
    assert is_accepted("Gosling berteriak keras") == True
    assert is_accepted("Chicco memanah burung cantik") == True
    assert is_accepted("Guru melahap apel dengan selahapnya") == True
    assert is_accepted("Mikasa melewati lembah dalam dengan berani") == True
    assert is_accepted("Hangralim berlatih sekerasnya") == True
    assert is_accepted("Candra mencuri mutiara indah") == True
    assert is_accepted("Turis tetap berjemur di pantai dengan teriknya matahari") == True
    assert is_accepted("Bayi menelan mentega dengan secepatnya") == True
    assert is_accepted("Anak itu menggambar dengan cepat") == True
    assert is_accepted("Amba melangkah secepatnya") == True
    assert is_accepted("Keisa menulis puisi indah") == True
    assert is_accepted("Guru menjelaskan materi dengan sejelasnya") == True
    assert is_accepted("Randi menjelaskan konsep sulit dengan sabar") == True
    assert is_accepted("Pegawai toko menyambut pelanggan dengan ramah") == True
    assert is_accepted("Peserta lomba melewati garis akhir dengan semangat") == True
    assert is_accepted("Petani tetap bekerja di ladang dengan panasnya cuaca") == True
    assert is_accepted("Dia merasa nyaman dalam kamar kotornya") == True
    assert is_accepted("Mahasiswa seharusnya menyelesaikan tugas dengan tepat waktu") == True
    assert is_accepted("Kamu sebaiknya memeriksa pekerjaanmu") == True
    assert is_accepted("Bryan makan dengan cepat") == True


def test_adjektival():
    assert is_accepted("Orang tua itu sangat kikir") == True
    assert is_accepted("Bahan baju tidur ini sangat lembut sekali") == True
    assert is_accepted("Kucing kecil itu lincah sekali") == True
    assert is_accepted("Bocah gemuk itu cukup gesit berlari di lapangan sekolah") == True
    assert is_accepted("Kopi itu terlalu panas untuk diminum") == True
    assert is_accepted("Harimau itu sangat ganas saat berburu") == True
    assert is_accepted("Aku sangat rindu kampung halaman") == True
    assert is_accepted("Anak itu sangat pintar dalam matematika") == True
    assert is_accepted("Rumah mereka terlalu besar untuk ditempati") == True
    assert is_accepted("Ruang tamu ini sangat lapang untuk rapat keluarga") == True
    assert is_accepted("Buku ini terlalu tebal untuk dibaca") == True
    assert is_accepted("Gedung-gedung baru itu sangat tinggi") == True
    assert is_accepted("Tingkat literasi para siswa itu masih sangat rendah") == True
    assert is_accepted("Kaos kaki adik saya sudah sangat longgar untuk digunakan") == True
    assert is_accepted("Suhu udara ini sangat dingin untuk berolahraga") == True
    assert is_accepted("Ruang belajar ini sangat sempit saat digunakan bersama") == True
    assert is_accepted("Harga makanan itu terlalu mahal untuk anak sekolah dasar") == True
    assert is_accepted("Pipi Doni itu biru lebam setelah dipukul Dodi") == True
    assert is_accepted("Warna buah jeruk itu oranye tua") == True
    assert is_accepted("Langit malam hari ini hitam pekat") == True
    assert is_accepted("Kacamata pria itu bulat") == True
    assert is_accepted("Bentuk wajah wanita ini terlalu lonjong") == True
    assert is_accepted("Laju pesawat terbang itu sangat cepat") == True
    assert is_accepted("Dia menyelesaikan tugas dalam waktu singkat") == True
    assert is_accepted("Teman saya itu sudah sangat lama menunggu") == True
    assert is_accepted("Ibu adik saya itu sangat cepat memasak nasi goreng") == True
    assert is_accepted("Hubungan pertemanan kami sangat dekat") == True
    assert is_accepted("Kota Atlantis itu sangat jauh dari kota kami") == True
    assert is_accepted("Keluarga saya sangat bahagia setelah adik kuliah") == True
    assert is_accepted("Ibu guru kami selalu bangga dengan prestasi muridnya") == True
    assert is_accepted("Teman Andi itu sangat bahagia saat diberikan kue") == True
    assert is_accepted("Para siswa itu sangat gembira menyambut hari libur") == True
    assert is_accepted("Dia sangat ragu-ragu dalam mengambil keputusan") == True
    assert is_accepted("Gadis kecil itu sangat cantik") == True
    assert is_accepted("Pemandangan Desa Buwit Tabanan itu sangat indah") == True
    assert is_accepted("Suara penyanyi Afgan itu sangat merdu sekali") == True
    assert is_accepted("Suara alunan musik klasik itu sangat lembut") == True
    assert is_accepted("Rasa sup sayur itu sangat lezat") == True
    assert is_accepted("Es teh lemon itu sangat segar") == True
    assert is_accepted("Aroma parfum ibu guru itu sangat harum") == True
    assert is_accepted("Baju merah itu sangat bagus") == True
    assert is_accepted("Rumah sederhana itu cukup indah") == True
    assert is_accepted("Gitar tua itu sangat mahal") == True
    assert is_accepted("Kucing putih itu sangat jinak") == True
    assert is_accepted("Mobil antik bapak itu sangat populer di kota kami") == True
    assert is_accepted("Gedung baru itu sangat megah") == True
    assert is_accepted("Lapangan bola itu cukup luas untuk bersepeda") == True
    assert is_accepted("Harga gedung baru itu cukup mahal") == True
    assert is_accepted("Sepatu anak itu sangat kecil") == True
    assert is_accepted("Kabar itu membuat mereka sangat gembira") == True
    assert is_accepted("Ayah mengecat pintu dapur dengan warna biru muda") == True
    assert is_accepted("Ibu selalu membelikan adik saya ikan segar") == True
    assert is_accepted("Kabar itu membuat mereka sangat bahagia") == True
    assert is_accepted("Roy membelikan saya mawar merah") == True
    assert is_accepted("Dia menganggap tugas itu susah") == True
    assert is_accepted("Anak itu bermain dengan gembira") == True
    assert is_accepted("Anjing itu menggonggong dengan sangat keras") == True
    assert is_accepted("Mobil itu berjalan sangat lambat") == True
    assert is_accepted("Gadis kecil itu menari dengan sangat gemulai") == True
    assert is_accepted("Anak itu menggambar dengan cepat") == True
    assert is_accepted("Amba melangkahkan kaki dengan sangat cepat") == True
    assert is_accepted("Bapak guru itu menjelaskan materi dengan sangat baik") == True
    assert is_accepted("Randi menjelaskan konsep sulit itu dengan sabar") == True
    assert is_accepted("Pegawai toko menyambut setiap pelanggan dengan ramah") == True
    assert is_accepted("Pemandangan matahari terbenam itu akan sangat menawan") == True
    assert is_accepted("Pertunjukan seni malam ini akan sangat indah") == True
    assert is_accepted("Semangat tim sepakbola itu sudah sangat tinggi") == True
    assert is_accepted("Suasana kerja kantor itu akan sangat nyaman") == True
    assert is_accepted("Anak kecil itu sedang sedih") == True
    assert is_accepted("Setiap orang itu pasti ingin selamat di dunia ini") == True
    assert is_accepted("Anak itu sangat kuat sekali") == True
    assert is_accepted("Jalan kampung itu becek sekali") == True
    assert is_accepted("Udara pagi hari ini cukup sejuk") == True
    assert is_accepted("Buku tebal itu sangat menarik untuk dibaca") == True
    assert is_accepted("Bunga kenanga itu sangat harum") == True
    assert is_accepted("Mobil cepat itu sangat mahal") == True
    assert is_accepted("Bunga itu masih segar di taman") == True
    assert is_accepted("Cuaca hari ini terlalu panas") == True
    assert is_accepted("Pertunjukkan tersebut sangat dramatis") == True
    assert is_accepted("Gedung itu dirancang dengan sangat megah") == True

    
def test_tidakbaku():
    assert is_accepted("Terlalu besar untuk ditempati") == False    
    assert is_accepted("Ruang tamu ini") == False    
    assert is_accepted("Terlalu tebal untuk dibaca") == False    
    # assert is_accepted("Gedung-gedung baru itu") == False    
    assert is_accepted("Masih sangat rendah") == False    
    assert is_accepted("Kaos kaki adik saya") == False    
    assert is_accepted("Dingin untuk berolahraga") == False    
    # assert is_accepted("Saat digunakan bersama") == False    
    assert is_accepted("Harga makanan itu") == False    
    assert is_accepted("Setelah dipukul Dodi biru lebab") == False    
    assert is_accepted("Menari dengan sangat gemulai") == False    
    assert is_accepted("Menggambar dengan cepat") == False    
    assert is_accepted("Melangkahkan kaki dengan sangat cepat") == False    
    assert is_accepted("Materi dengan sangat baik") == False    
    # assert is_accepted("Konsep sulit itu dengan sabar") == False    
    assert is_accepted("Pegawai toko sedang") == False    
    # assert is_accepted("Pemandangan matahari terbenam itu") == False    
    assert is_accepted("Pertunjukan seni malam ini") == False    
    assert is_accepted("Semangat tim sepakbola itu") == False    
    assert is_accepted("Suasana kerja di kantor itu akan sangat nyaman") == False    
    assert is_accepted("Sedang sedih") == False    
    assert is_accepted("Setiap orang itu") == False    