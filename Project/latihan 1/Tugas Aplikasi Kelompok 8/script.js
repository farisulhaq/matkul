function validate(){
    // ambil nilai
    var nama = document.getElementById('user');
    var email = document.getElementById('email');
    var hp = document.getElementById('telep');
    var tgl = document.getElementById('tgl');
    var pay = document.getElementsByName('metode');
    // tempat Jalan eror
    var namaerror = document.getElementById('namaerr');
    var emailerror = document.getElementById('emailerr');
    var hperror = document.getElementById('hperr');
    var tglerror = document.getElementById('tglerr');
    var payerror = document.getElementById('payerr');
    // Eror line
    var namaerr = "";
    var emailerr = "";
    var hperr = "";
    var tglerr = "";
    var payerr = "";
    // cek nama
    if (nama.value == "") {
        namaerr = "Nama Belum Diisi";
        namaerror.className = "erorr";
        nama.style.border = "2px solid red";
        namaerror.innerHTML = namaerr;
    } else {
        nama.style.border = "2px solid green";
    }
    // cek Email
    if (email.value == "") {
        emailerr = "Email Belum Diisi";
        emailerror.className = "erorr";
        email.style.border = "2px solid red";
        emailerror.innerHTML = emailerr;
    } else {
        email.style.border = "2px solid green";
    }
    // cek Hp
    if (hp.value == "") {
        hperr = "Nomer Hp Belum Diisi";
        hperror.className = "erorr";
        hp.style.border = "2px solid red";
        hperror.innerHTML = hperr;
    } else {
        hp.style.border = "2px solid green";
    }
    // Cek tgl
    if (tgl.value == "") {
        tglerr = "Tangal Lahir Belum Diisi";
        tglerror.className = "erorr";
        tgl.style.border = "2px solid red";
        tglerror.innerHTML = tglerr;
    } else {
        tgl.style.border = "2px solid green";
    }
    // cek Pembayaran
    var temp = 0;
    for (var i = 0; i < pay.length; i++) {
        if (pay[i].checked) {
            temp += 1;
        }
    }
    if (temp == 0) {
        payerr = "Anda Belum Memilih Metode Pembayaran";
        payerror.className = "erorr";
        payerror.innerHTML = payerr;
    }
    // cek eror line
    if ((namaerr != "") || (emailerr != "") || (hperr != "") || (tglerr != "") || (payerr != "")) {
        return false;
    } 
}
function hapusError(id,eror) {
    document.getElementById(eror).innerHTML = "";
    document.getElementById(id).style.border = "";
}
function radioError() {
    alert(payerr)
    payerr.innerHTML = "";
}