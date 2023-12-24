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