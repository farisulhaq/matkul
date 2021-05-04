// Fungsi nextFa checkbox > 1
function nextFa(name,showTrue,showFalse,hide) {
    var nama = document.getElementsByName(name);
    var temp = 0;
    for (var i = 0; i < nama.length; i++) {
        if (nama[i].checked) {
            temp++;
        }
    }
    if (temp >= 3) {
        document.getElementById(showTrue).style.display = "block";
    } else {
        document.getElementById(showFalse).style.display = "block";
    }
    document.getElementById(hide).style.display = "none";
    return false;
}
// fungsi nextFz checkbox >= 1
function nextFz(name,showTrue,showFalse,hide) {
    var input = document.getElementsByName(name);
    var num = false;
    for (var i = 0; i < input.length; i++) {
        if (input[i].checked) {
            num = true;
        }
    }
    if (num) {
        document.getElementById(showTrue).style.display = "block";
    } else {
        document.getElementById(showFalse).style.display = "block";
    }
    document.getElementById(hide).style.display = "none";
    return false;
}
// Fungsi back
function backFa(backShow,backHide) {
    document.getElementById(backShow).style.display = "block";
    document.getElementById(backHide).style.display = "none";
    return false;
}
// refres
function logout() {
    location.replace("covid.html")
}