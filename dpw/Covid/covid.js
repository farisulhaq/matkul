function slideNext(idt,idTrue,idFalse,hide) {
    var idn = document.getElementsByName(idt);
    var temp = 0;
    for (var i = 0; i < idn.length; i++) {
        if (idn[i].checked) {
            temp++;
        }
    }
    if (temp >= 3 ) {
        document.getElementById(idTrue).style.display = "block";
    }else {
        document.getElementById(idFalse).style.display = "block";
    }
    document.getElementById(hide).style.display = "none";
    return false;
}
function nextSlide(idt,idTrue,idFalse,hide) {
    var input = document.getElementsByName(idt);
    var num = false;
    for (var i = 0; i < input.length; i++) {
        if (input[i].checked) {
            num = true;
        }
    }
    if (num) {
        document.getElementById(idTrue).style.display = "block";
    } else {
        document.getElementById(idFalse).style.display = "block";
    }
    document.getElementById(hide).style.display = "none";
    return false;
}
function back(backShow,backHide) {
    document.getElementById(backShow).style.display = "block";
    document.getElementById(backHide).style.display = "none";
    return false;
}
function refres() {
    location.replace("covid.html");
}