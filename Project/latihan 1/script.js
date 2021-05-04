function onFormSubmit(){
    var data = database();
    insert(data);
}

function database(){
    var  data = {};
    data["nama"] = document.getElementById("nama").value;
    data["nim"] = document.getElementById("nim").value;
    data["kelas"] = document.getElementById("kelas").value;
    return data
}

function insert(data){
    var tabel = document.getElementById("list").getElementsByTagName("tbody")[0];
    var newdata = tabel.insertRow(tabel.length);
    cell1 = newdata.insertCell(0);
    cell1.innerHTML = data.nama;
    cell2 = newdata.insertCell(1);
    cell2.innerHTML = data.nim;
    cell3 = newdata.insertCell(2);
    cell3.innerHTML = data.kelas;

}