window.onload = function(){
    btn_post = document.querySelector('.btn-post');
    btn_photo = document.querySelector('.btn-photo');
    btn_subscriptions = document.querySelector('.btn-subscriptions');
    btn_subscribers = document.querySelector('.btn-subscribers');
    profile_post = document.querySelector('.profile-post');
    profile_photo = document.querySelector('.profile-photo');
    profile_subscriptions = document.querySelector('.profile-subscriptions');
    profile_subscribers = document.querySelector('.profile-subscribers');

    btn_post.addEventListener('click', function(){
        profile_post.style.display = 'flex';
        profile_photo.style.display = 'none';
        profile_subscriptions.style.display = 'none';
        profile_subscribers.style.display = 'none';
    });
    btn_photo.addEventListener('click', function(){
        profile_post.style.display = 'none';
        profile_photo.style.display = 'flex';
        profile_subscriptions.style.display = 'none';
        profile_subscribers.style.display = 'none';
    });
    btn_subscriptions.addEventListener('click', function(){
        profile_post.style.display = 'none';
        profile_photo.style.display = 'none';
        profile_subscriptions.style.display = 'flex';
        profile_subscribers.style.display = 'none';
    });
    btn_subscribers.addEventListener('click', function(){
        profile_post.style.display = 'none';
        profile_photo.style.display = 'none';
        profile_subscriptions.style.display = 'none';
        profile_subscribers.style.display = 'flex';
    });
}