window.onload = function(){
    btn_post = document.querySelector('.btn-post');
    btn_photo = document.querySelector('.btn-photo');
    btn_friend = document.querySelector('.btn-friend');
    profile_post = document.querySelector('.profile-post');
    profile_photo = document.querySelector('.profile-photo');
    profile_friend = document.querySelector('.profile-friend');


    btn_post.addEventListener('click', function(){
        profile_post.style.display = 'flex';
        profile_photo.style.display = 'none';
        profile_friend.style.display = 'none';
    });
    btn_photo.addEventListener('click', function(){
        profile_post.style.display = 'none';
        profile_photo.style.display = 'flex';
        profile_friend.style.display = 'none';
    });
    btn_friend.addEventListener('click', function(){
        profile_post.style.display = 'none';
        profile_photo.style.display = 'none';
        profile_friend.style.display = 'flex';
    });
}