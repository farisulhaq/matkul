// console.log('saya')
// var nama = prompt('saya :')
// alert('selamat datang '+nama);
// confirm('yakin?')

// var start = true
// while(start){
//     var a = prompt('masukkan angka :')
//     if(a % 2 == 0){
//         alert('angka ' + a + 'adalah bilangan genap')
//     }else{
//         alert('angka ' + a + 'adalah bilangan ganjil')
//     }
//     start = confirm('lagi ?')
// }

// var a = 1
// while(a <= 10){
//     console.log(`Angka No. ${a} beroperasi dengan baik`)
//     a++;
// }

// for (a = 1; a <=10; a++) {
//     if (a < 6) {
//         console.log(`Angkot No. ${a} beroperasi dengan baik`)
//     }else {
//         console.log(`Angkot No. ${a} beroperasi dengan tidak baik`)
//     }
// }

var x = ''
for ( a = 0; a <= 6; a++ ) {
    for ( b = 0; b < a; b++ ) {
        x += '*'
    }
    x += '\n'
}
console.log(x)

var y = ''
for ( a = 0; a <= 6; a++ ) {
    for ( b = 0; b < 6-a; b++ ) {
        y += '*'
    }
    y += '\n'
}
console.log(y)

var y = ''
x = 6
for ( a = 0; a < 6; a++ ) {
    for ( b = 0; b <= x-1; b++ ) {
        y += ' '
    }
    x -= 1
    for ( b = 0; b <= a; b++ ) {
        y += '*'
    }
    y += '\n'
}
console.log(y)

var y = ''
x = 6
for ( a = 0; a < 6; a++ ) {
    for ( b = 0; b <= a; b++ ) {
        y += ' '
    }
    for ( b = 0; b <= x-1; b++ ) {
        y += '*'
    }
    x -= 1
    y += '\n'
}
console.log(y)

y += ""
var x = 5;
for (var i = 0; i < x; i++){
    for (var y = 1; y < (x - i); y ++){
        document.write("")
        y += ' '
    }
    for (var j = 0; j < (i*2)+1;j++){
        document.write("*")
        y += '*'
    }
    document.write("<br>")
    y += '\n'
}
console.log(y)
// var baris, i = 0;
// var nilai_prompt = prompt("Tinggi: ", ""); 
// var tinggi=parseInt(nilai_prompt);

// for (baris = 0; baris <= tinggi ; baris++) {

// // memBuat sejumlah spasi
// for (i = 1; i <= tinggi - baris; i++) {
// document.write(" "); // Karakter spasi
//     }

// // menampilkan bintang
// for (i = 1; i < 2 * baris; i++) {
// document.write("*"); }

// // Pindah baris
// document.write("\n"); }