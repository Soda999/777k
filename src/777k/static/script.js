$(document).ready(function(){
    $('#67').on('submit', function(e){
        e.preventDefault();
        
        if ($('#password').val() !== $('#confirm_password').val()){
            alert('Пароли не совпадают!');
            return;
        }
        
        $.ajax({
            url: '/user_register',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                name: $('#fullname').val(),
                password: $('#password').val(),
                email: $('#email').val()
            }),
            success: function(response){
                alert('Регистрация успешна!');
                window.location.href = '/login';
            },
            error: function(xhr){
                alert('Ошибка регистрации: ' + xhr.status);
            }
        });
    });
});

$(document).ready(function(){
    $('#76').on('submit', function(e){
        e.preventDefault();
        
        $.ajax({
            url: '/user_login',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                password: $('#password').val(),
                email: $('#email').val()
            }),
            success: function(response){
                alert('Вы вошли!');
            },
            error: function(xhr){
                alert('Ошибка входа: ' + xhr.status);
            }
        });
    });
});