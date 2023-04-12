//function check_form() {
// var form= document.forms['login-form'];
// if(form.ID.value =='gitcha2' && form.password.value=="1234")
// {
//   window.open('main.html');
//   return true;
// }
// else{
//       alert("아이디랑 비밀번호를 확인해 주세요");
//       return false;
// }
//}

// KKH 추가 23.04.12
function check(){
    var form = document.forms['login-form'];

    if(!form.memberId.value){
        alert("아이디를 입력해주세요.");
        form.memberId.focus();
        return;
    }

    if(!form.memberPw.value){
        alert("비밀번호를 입력해주세요.");
        form.memberPw.focus();
        return ;
    }
    form.submit();

}
