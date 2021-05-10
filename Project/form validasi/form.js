function checkName(){
	var nama=document.getElementById("user")
	var namerr=document.getElementById("userMissing")
	if((nama.value)==""){
		namerr.style.visibility="visible";
		nama.style.border="2px solid red"
		nama.focus();
		return false
	}
	else{
		nama.style.border="2px solid green"
		return true
	}
}
	
function checkMail(){
	var mail=document.getElementById("email")
	var mailerr=document.getElementById("emailMissing")
	if((mail.value)==""){
		mailerr.style.visibility="visible";
		mail.style.border="2px solid red";
		mail.focus();
		return false	
	}
	else{
		
		return true
	}
}

function checkError(a,b){
	if((document.getElementById(a).value)!=""){
		document.getElementById(b).style.visibility="hidden";
		document.getElementById(a).style.border="2px solid green";
	}
}

function validateForm(){
	var namanya = checkName();
	var emailnya = checkMail();	
	if(namanya&&emailnya){
	// if ((name===true&&email===true)){
		return true
	}
	return false
}