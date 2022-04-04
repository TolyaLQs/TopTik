window.onload = function(){
    my_following = document.querySelector('.my-following');
    my_fol_tit_span = document.querySelector('.my-fol-tit-span');
    my_following.addEventListener('mouseover', function(e){
        my_following.style.width = '200px';
        my_fol_tit_span.style.display = 'flex';
    });
    my_following.addEventListener('mouseout', function(e){
        my_following.style.width = '50px';
        my_fol_tit_span.style.display = 'none';
    });
}