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
        y += '* '
    }
    x -= 1
    y += '\n'
}
console.log(y)