function validate(){
	//mengambil nilai inputan
	var namatim= document.getElementById("Nama_tim")
	var namaket = document.getElementById( "Nama_ketua" );
	var nomor= document.getElementById("nomor")
	var male = document.getElementById( "male" );
	var female = document.getElementById("female");
	var kota= document.getElementById("kota");
	var mail=document.getElementById('mail')
	var anggota_1=document.getElementById('Anggota1')
	var anggota_2=document.getElementById('Anggota2')
	var angmale1=document.getElementById('male1')
	var angfemale1=document.getElementById('female1')
	var angmale2=document.getElementById('male2')
	var angfemale2=document.getElementById('female2')
	var tanggal=document.getElementById('tgl')
	var box=document.getElementById('box')

	//error
	var namatimError='';
	var Nama_ketuaError='';
	var jkError='';
	var kotaError='';
	var Nomorerror='';
	var mailError='';
	var angErr1='';
	var angErr2='';
	var tglErr='';
	var boxErr='';
	var anggota1Err='';
	var anggota2Err='';
	//cek nama tim
	if (namatim.value == "")
	{
		namatimError ="Anda belum mengisi nama tim"
		namatimError.className="namatimError";
		namatim.style.border="2px solid red";
		document.getElementById( "namatimError" ).innerHTML = namatimError;
	}
	else if (Nama_tim.value.trim().length<6) {
		namatimError ="Nama tim minimal 6 karakter"
		namatimError.className="namatimError";
		namatim.style.border="2px solid red";
		document.getElementById( "namatimError" ).innerHTML = namatimError;
	}
	else{
		Nama_tim.style.border="2px solid green"
	}
	//cek nama ketua
	if( namaket.value == "" )
	{
		Nama_ketuaError = "Anda belum mengisi nama ketua";
		Nama_ketuaError.className="Nama_ketuaError";
		namaket.style.border="2px solid red";
		document.getElementById( "Nama_ketuaError" ).innerHTML = Nama_ketuaError;
	}
	else{
		Nama_ketua.style.border="2px solid green"
		Nama_ketuaError.innerHTML=""
	}
	//cek jenis kelamin
	if (male.checked==false && female.checked ==false) {
		jkError = "Anda belum memilih jenis kelamin";
		jkError.className="jkError";
		document.getElementById( "jkError" ).innerHTML = jkError;
	}
	//cek kota
	if (kota.value=='-') {
		kotaError = "Anda belum memilih kota anda";
		kotaError.className="kotaError";
		document.getElementById( "kotaError" ).innerHTML = kotaError;
	}
	//cek nomor telepon
	if( nomor.value == "")
	{
		Nomorerror="Anda belum mengisi nomor"
		Nomorerror.className="Nomorerror";
		nomor.style.border="2px solid red"
		document.getElementById( "Nomorerror" ).innerHTML = Nomorerror;
	}
	else if (nomor.value.trim().length < 10 || nomor.value.trim().length >12) {
		Nomorerror="format nomor yang anda masukkan salah"
		Nomorerror.className="Nomorerror";
		nomor.style.border="2px solid red"
		document.getElementById( "Nomorerror" ).innerHTML = Nomorerror;
	}
	else{
		nomor.style.border="2px solid green"
	}
	//cek email
	var cek=/^\w+[\+\.\w-]*@([\w-]+\.)*\w+[\w-]*\.([a-z]{2,4}|\d+)$/i
	var hasil=cek.test(mail.value)
	if (hasil==false){
		mailError = "email tidak valid";
	   	mailError.className="mailError";
		mail.style.border="2px solid red"
		document.getElementById( "mailError" ).innerHTML = mailError;
	}
	else{
		mail.style.border="2px solid green"
	}
	//cek data anggota 1
	if (anggota_1.value!=''){
		if (male1.checked==false && female1.checked==false) {
			angErr1 = "Anda belum memilih jenis kelamin anggota 1";
			angErr1.className="angErr1";
			document.getElementById( "angErr1" ).innerHTML = angErr1;
		}
	}
	//cek data anggota 2
	if (anggota_2.value!='') {
		if (male2.checked==false && female2.checked==false){
			angErr2 = "Anda belum memilih jenis kelamin anggota 2";
			angErr2.className="angErr2";
			document.getElementById( "angErr2" ).innerHTML = angErr2;
		}
	}
	//cek inputan tanggal
	var patt=/^(199[7-9]|200[0-2])[-/](0[1-9]|1[012])[-/](0[1-9]|[12][0-9]|3[01])$/g;
	var cektgl=patt.test(tanggal.value)
	if (cektgl==false) {
		tglErr='tanggal yang anda masukkan salah';
		tglErr.className='tglErr';
		tgl.style.border='2px solid red'
		document.getElementById("tglErr").innerHTML=tglErr;
	}
	else{
		tgl.style.border='2px solid green'
	}
	//cek input checkbox
	if (box.checked==false){
		boxErr= 'Syarat dan ketentuan harus di setujui'
		boxErr.className='boxErr'
		document.getElementById("boxErr").innerHTML=boxErr;
	}
	//jika ada error maka tidak bisa di submit
	if (namatimError != '' || Nama_ketuaError != '' || jkError != ''|| kotaError != '' || Nomorerror != '' || mailError!='' || angErr1 !='' || angErr2!='' || boxErr!='' || anggota1Err!='' || anggota2Err!='') {
		return false;
	}
	else
	{
		return true;
		}
    }
//cek inputan huruf nama ketua
function string(e) {
 	if ((e.keyCode!=13) &&  (e.keyCode < 65) || (e.keyCode > 90 && e.keyCode <97) || (e.keyCode >122) ) {
   		Nama_ketuaError = "Inputan nama harus huruf";
  		Nama_ketuaError.className="Nama_ketuaError";
		Nama_ketua.style.border="2px solid red";
		document.getElementById( "Nama_ketuaError" ).innerHTML = Nama_ketuaError;
		return false;
	 	}
	 else
	 	{
	 	Nama_ketuaError = "";
	   	Nama_ketuaError.className="Nama_ketuaError";
		Nama_ketua.style.border=""
		document.getElementById( "Nama_ketuaError" ).innerHTML = Nama_ketuaError;
 }
}

//cek nama anggota1
function string2(e) {
 	if ( (e.keyCode!=13) && (e.keyCode < 65) || (e.keyCode > 90 && e.keyCode <97) || (e.keyCode >122) ) {
   		anggota1Err = "Inputan Nama anggota 1 harus huruf";
  		anggota1Err.className="anggota1Err";
		Anggota1.style.border="2px solid red";
		document.getElementById( "anggota1Err" ).innerHTML = anggota1Err;
		return false;
	 	}
	 else
	 	{
	 	anggota1Err = "";
  		anggota1Err.className="anggota1Err";
		Anggota1.style.border="2px solid green";
		document.getElementById( "anggota1Err" ).innerHTML = anggota1Err;
  		return true;
 }
}

//cek nama anggota2
function string3(e) {
 	if ( (e.keyCode!=13) && (e.keyCode < 65) || (e.keyCode > 90 && e.keyCode <97) || (e.keyCode >122) ) {
   		anggota2Err = "Inputan nama anggota 2 harus huruf";
  		anggota2Err.className="anggota1Err";
		Anggota2.style.border="2px solid red";
		document.getElementById( "anggota2Err" ).innerHTML = anggota2Err;
		return false;
	 	}
	 else
	 	{
	 	anggota2Err = "";
  		anggota2Err.className="anggota2Err";
		Anggota2.style.border="2px solid green";
		document.getElementById( "anggota2Err" ).innerHTML = anggota2Err;
  		return true;
 }
}

//cek inputan angka
function integer(e) {
	if ((e.keyCode!=13) && (e.keyCode < 48) || (e.keyCode >57) || (e.keyCode ==15)) {
	   	Nomorerror = "Inputan harus angka";
		nomor.style.border="2px solid red"
		document.getElementById( "Nomorerror" ).innerHTML = Nomorerror;
		return false
	    }
	else
		{
		Nomorerror = "";
	   	Nomorerror.className="Nomorerror";
		nomor.style.border=""
		document.getElementById( "Nomorerror" ).innerHTML = Nomorerror;
	return true;
		}
	}

//menghapus error jenis kelamin dan kota
function hapusError(e){
	if (male.checked==true || female.checked ==true){
		jkError.innerHTML="";
	}
	if (kota.value!="-"){
		kotaError.innerHTML="";
	}
	if (male1.checked==true || female1.checked == true){
		angErr1.innerHTML='';
	}
	if (male2.checked==true || female2.checked == true){
		angErr2.innerHTML='';
	}
	if (box.value=true) {
		boxErr.innerHTML='';
	}
}

//menghapus nama tim error
function hapusNamatimError(e){
	namatimError.innerHTML=""
	e.target.style.border=""
}
function hapusNamaKetuaError(e){
	Nama_ketuaError.innerHTML=""
	e.target.style.border=""
}
function hapusMailerror(e){
	mailError.innerHTML=''
	e.target.style.border=""
 }
function hapusTglErr(e){
	tglErr.innerHTML=''
	e.target.style.border=''
 }
