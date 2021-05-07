function tes1() {
    var x = [];
    var awal = 10;
    var akhir = 50;
    // membuat bilangan genap antara 10 - 50
    for (awal; awal <= akhir; awal++) {
        if (awal % 2 == 0) {
            x.push(awal);
        }
    }
    // melakukan operasi matematika z = 2x + 15x
    var temp = "";
    var jml = 0;
    for (i in x) {
        z = 2*x[i] + 15*x[i];
        jml += z;
        temp += `z = 2(${x[i]}) + 15(${x[i]}) = ${z} <br>`
    }
    document.getElementById("tes1").innerHTML = temp +"<br> jumlah z = " + jml;
}

function tes2() {
    // Soal Nomer 2
    var hasil = [];
    var a = parseInt(document.getElementById("a").value);
    var b = parseInt(document.getElementById("b").value);
    for (var i = 1; i <= 20; i++) {
        hasil.push(Math.floor(Math.random() * (b - a + 1)) + a);
    }
    document.getElementById("tes2").innerHTML = "["+hasil+"]";
    // Soal Nomer 3
    // urut nilai list
    hasil.sort(function(a,b){return a - b});
    document.getElementById("arr").innerHTML = hasil;
    // Nilai MIn
    var min = hasil[0];
    for (x in hasil) {
        if (min > hasil[x]) {
            min = hasil[x];
        }
    }
    document.getElementById("min").innerHTML = min;
    // Nilai Max
    var max = hasil[0];
    for (x in hasil) {
        if (max < hasil[x]) {
            max = hasil[x];
        }
    }
    document.getElementById("max").innerHTML = max;
    // Nilai Mean
    var mean = 0;
    for (x in hasil) {
        mean += hasil[x];
    }
    document.getElementById("mean").innerHTML = mean/hasil.length;
    // Nilai Median
    var med = Math.floor(hasil.length/2);
    var median;
    if (hasil.length % 2 == 0) {
        median = (hasil[med]+hasil[med-1])/2;
    } else {
        median = hasil[med];
    }
    document.getElementById("median").innerHTML = median;
    // Nilai Modus
    var temp = {};
    var modus = [];
    var maks = 0;
    for (var i in hasil) {
        temp[hasil[i]] = (temp[hasil[i]] || 0) + 1;
        if (temp[hasil[i]] > maks) {
            maks = temp[hasil[i]];
        }
    }
    // cek nilai Modus
    for (var i in temp) {
        if (temp[i] == maks) {
            modus.push(i);
        }
    }
    if (maks == 1) {
        modus = "Modus Tidak Ada";
    }
    document.getElementById("modus").innerHTML = modus;
    return false;
}
function hapus(id) {
    document.getElementById(id).innerHTML = "";
}