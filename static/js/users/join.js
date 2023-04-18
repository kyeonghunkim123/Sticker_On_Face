
// 가입부분 체크

function check_from(){

  let name = document.getElementById("name").value
  let ID = document.getElementById("user_ID").value
  let password = document.getElementById("user_password").value
  let Email = document.getElementById("mail").value
   // 이메일확인

  if(name == ''){
  alert('이름을 입력해 주세요')
  else{
  alert('이름을 다시 입력해주세요')}}

  if(ID == ''){
  alert('아이디를 입력해 주세요')}
  else{
  alert('아이디를 다시 입력해주세요')}

  if(password == ''){
  alert('비밀번호를 입력해 주세요')}
  else{
  alert('비밀번호를 다시 입력해주세요')}
  }
  if(Email.includes('@')){
    let emailId = email.split('@')[0]
    let emailServer = email.split('@')[1]
    if(emailId === "" || emailServer === ""){
      document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다."
      check = false





