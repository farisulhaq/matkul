// Fungsi untuk mengecek checkbox > 3
function nextFa(name,showTrue,showFalse,hide) {
    var nama = document.getElementsByName(name); // menyimpan dari elements name
    var temp = 0; // variebel temp = 0
    // perulangan untuk cek ceklis tidaknya di checkbox
    for (var i = 0; i < nama.length; i++) {
        // pengecekan true checkbox
        if (nama[i].checked) {
            // jika true makan temp + 1
            temp++;
        }
    }
    // pengecekan jika temp sama dengan 3 atau lebih
    if (temp >= 3) {
        // jika true maka 
        document.getElementById(showTrue).style.display = "block"; // merubah display dari none ke block
    } else {
        // jika false maka
        document.getElementById(showFalse).style.display = "block"; // merubah display dari none ke block
    }
    // menghide tampilan yang sedang terbuka setelah mengklik tombol
    document.getElementById(hide).style.display = "none"; // merubah display dari block ke none
    return false;
}
// fungsi untuk mengecek checkbox >= 1
function nextFz(name,showTrue,showFalse,hide) {
    var input = document.getElementsByName(name); // menyimpan dari elements name
    var num = false; // variebel temp = false
    // perulangan untuk cek ceklis tidaknya di checkbox
    for (var i = 0; i < input.length; i++) {
        // pengecekan true checkbox
        if (input[i].checked) {
            // jika true makan num sama dengan true
            num = true;
        }
    }
    // pengecekan num true atau false
    if (num) {
        // jika true maka
        document.getElementById(showTrue).style.display = "block"; // merubah display dari none ke block
    } else {
        // jika false maka
        document.getElementById(showFalse).style.display = "block"; // merubah display dari block ke none
    }
    // menghide tampilan yang sedang terbuka setelah mengklik tombol
    document.getElementById(hide).style.display = "none";
    return false;
}
// Fungsi back
function backFa(backShow,backHide) {
    document.getElementById(backShow).style.display = "block"; // merubah display dari none ke block
    document.getElementById(backHide).style.display = "none"; // merubah display dari block ke none
    return false;
}
// refres
function logout() {
    location.replace("covid.html")
}