var n = 3
var start = true
alert('tebak angka 1 - 10\nkamu mempunyai ' + n + ' kesempatan')
var tebak = Math.floor(Math.random() * 10) + 1;
while ( start ) {
    var a = parseInt(prompt('masukkan angka tebakan :'))
    var hasil = ''
    if ( a < tebak ) {
        hasil = 'terlalu RENDAH'
    } else if ( a == tebak ) {
        hasil = 'anda BENAR'
    } else if ( a > tebak ) {
        hasil = 'terlalu BESAR'
    } else {
        hasil = 'anda tidak memasukkan angka' 
    }
    n--;
    var pesan = ''
    if ( n !== 0 ) {
        pesan = 'anda memiliki ' + n + ' kesempatan lagi'
    } else {
        pesan = 'kesempatan anda habis'
        start = false
    }
    if ( a === tebak ) {
        alert(hasil + '\nangka yang di cari adalah ' + tebak)
        alert('terima kasih boys')
        start = false
    } else {
        alert(hasil + '\n' + pesan + tebak)
        if ( n === 0 ) {
            alert('anda gagal \nangka yang di cari ' + tebak)
        }
    }
    
}