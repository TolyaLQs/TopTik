
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
                if (data['active']){
                    like_div.classList.add("active");
                }else{
                    like_div.classList.remove("active");
                }
            }
        }
    });
}

window.onload = function() {

}

