/* Log In */

$(function(){
    $("#check_login").click(function(){
        console.log("--0--");
        var userid = $('#id').val();
        var userpw = $('#pwd').val();
        console.log(userid);


        if (userid === ''){
            alert('아이디를 입력하세요');
            return false;
        }
        if (userpw === ''){
            alert('비밀번호를 입력하세요');
            return false;
        }
        var csrf_token = "{{ csrf_token }}";
        console.log("--1--");
        $.ajax({
            url:'/check_login/',
            type:'POST',
            headers: {'X-CSRFToken': csrf_token},
            data:{
                  'userid':userid,
                  'userpw':userpw,
                  'csrfmiddlewaretoken': csrf_token
            },
            success:function(response){
                console.log("--2--");
                if(response['success'] == 'True'){

                    alert('아이디나 비밀번호가 올바르지 않습니다');

                }
                else{
                    console.log("--3--");
                    alert('로그인에 성공했습니다');
                    location.href = 'http://127.0.0.1:8000/';

                }
            }
        });
    });
});


/* Find ID */

$(function() {
    $("#next").click(function() {
        var username = $('#name').val();
        var usertel = $('#tel').val();

        if (username === '') {
            alert('아이디를 입력하세요');
            return false;
        }
        if (usertel === '') {
            alert('전화번호를 입력하세요');
            return false;
        }

        var csrf_token = "{{ csrf_token }}";
        $.ajax({
            url: '/find_myid/',
            type: 'POST',
            headers: {'X-CSRFToken': csrf_token},
            data: {
                'username': username,
                'usertel': usertel,
                'csrfmiddlewaretoken': csrf_token
            },
            success: function(response) {
                if (response.success === 'True') {
                    alert('성공.');
                    var userid = response.userid;
                    $('#result').text('아이디는 ' + userid + ' 입니다.');
                } else {
                    alert('이름이 일치하지 않습니다.');
                    location.href = 'http://127.0.0.1:8000/users/find_id'

                }
            }
        });
    });
});


/* SignUp */

$(function(){
    $("#signup_button").prop("disabled", true);

    $("#check_Id").click(function(){
        var userid = $('#user_ID').val();
        console.log("userId : " + userid);
        if (userid === ''){
            alert('아이디를 입력하세요');
            return false;
        }
        var csrf_token = "{{ csrf_token }}";
        $.ajax({
            url:'/check_Id/',
            type:'POST',
            headers: {'X-CSRFToken': csrf_token},
            data:{'userid':userid,
                  'csrfmiddlewaretoken': csrf_token
            },
            success:function(request){
                if(request['exists'] == 'True'){

                    alert('중복되는 아이디가 있습니다');
                    $('#user_ID').focus()
                }
                else{
                    alert('사용가능한 아이디입니다');
                    $("#signup_button").prop("disabled", false);
                }
            }
        });
    });
});

$(function(){
    $("#signup_button").click(function(){


        var username = $('#name').val();
        var userid = $('#user_ID').val();
        var userpw = $('#user_password').val();
        var userphone = $('#phone').val();
        var usermail = $('#mail').val();

        if (username === ''){
            alert('이름를 입력하세요');
            return false;
        }
        if (userpw === ''){
            alert('비밀번호를 입력하세요');
            return false;
        }
        if (!/^[\d-]+$/.test(userphone)) {
    		alert('휴대폰번호는 숫자만 입력 가능합니다.');
    		return false;
        }
        if (usermail === ''){
            alert('이메일를 입력하세요');
            return false;
        }
        if (!usermail.includes("@")) {
            alert('올바른 이메일 주소를 입력하세요');
            return false;
        }
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url:'/check_join/',
            type:'POST',
            headers: {'X-CSRF-Token': csrf_token},
            data:{
                'username':username,
                'userid':userid,
                'userpw':userpw,
                'userphone':userphone,
                'usermail':usermail,
                'csrfmiddlewaretoken': csrf_token
            },
            success:function(response){
                if(response['success'] == 'True'){
                    alert('회원가입에 성공을 했습니다.');
                    location.href = 'http://127.0.0.1:8000/';
                }
                else{
                    alert('회원가입을 다시해주세요');
                }
            },
            error:function(error){
            	console.log(error);
                alert('회원가입에 실패하였습니다. 에러: ' + error.responseText);
                window.location.href = '';
            }
        });
    });
});