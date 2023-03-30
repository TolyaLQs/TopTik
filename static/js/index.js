
function like(post_id, user_id) {
    $.ajax({
        url: '/postaddlike/',
        headers: {'X-CSRFToken': document.getElementById('csrf').querySelector('input').value},
        data: {post: post_id, user: user_id,},
        type: "POST",
        dataType: 'json',
        success: function (data) {
            if (data) {
                like_div = document.getElementById("like-post" + '-' + post_id);
                like_div.children[1].innerHTML = data['quantity'];
            }
        }
    });
//    console.log('like', post_id, " ", user_id);
//    $.post('/postaddlike/',{ // постом отпровляем ассоциативный массив данных в на сервер
//            post_id: post_id,
//            user_id: user_id,
//        }, function(response){
//            console.log(response);
//            if('error'==response.result){ //если есть ошибки то они отображаются
//
//            } else { // если нет ошибок показывается див с текстом об успешной отправки
//
//            }
//        });
}

window.onload = function() {

}

