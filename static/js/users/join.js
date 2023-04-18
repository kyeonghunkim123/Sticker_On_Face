
function check_from(){
	let name = document.getElementById("name").value
	let ID = document.getElementById("user_ID").value
	let password = document.getElementById("user_password").value
    let phone = document.getElementById("phone").value
	let Email = document.getElementById("mail").value
	if(name == ''){
		alert('이름을 입력해 주세요')
	return false;
	}
    if(ID == ''){
		alert('아이디를 입력해주세요');
	return false;
	}
    if(password == ''){
		alert('비밀번호를 입력해주세요');
	return false;
	}
	if(phone == ''){
		alert('전화번호를 입력해 주세요');
	return false;
	}
	if(Email == ''){
		alert('이메일을 입력해주세요');
	return false;
	}
    return true;
}
