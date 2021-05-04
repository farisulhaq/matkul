var mahasiswa = ["Ahmad Farisul Haq",200411100171,"Universita Trunojoyo Madura"];
var temp = "";
for (var i = 0; i < mahasiswa.length; i++) {
    temp += mahasiswa[i] + "<br>";
} 
document.getElementById("arr").innerHTML = temp;
