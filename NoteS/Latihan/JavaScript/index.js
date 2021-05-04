function cekName() {
	var nama = document.getElementById("name").value;
	if (nama == ""){
		document.getElementById("nameMissing").style.visibility = "visible";
        document.getElementById("name").focus();
        return false;
	}
    return true;
}
function cekValue() {
    var nama = document.getElementById("name").value;
	if (nama != ""){
		document.getElementById("nameMissing").style.visibility = "hidden";
	}
}
function cekPassword() {
    var pw = document.getElementById("pw").value;
    var cpw = document.getElementById("cpw").value;
    if (pw != cpw) {
        document.getElementById("pesan").style.visibility = "visible";
        return false;
    } else if (pw == "") {
        document.getElementById("eror").innerHTML = "Password is a required field";
    }
    return true;
}
function validasi(){
    var a = cekName();
    var b = cekPassword();
    if (a && b) {
        return true
    }
    return false
}