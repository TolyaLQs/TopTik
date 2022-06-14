window.onload = function(){
    step1 = document.querySelector('.step-1');
    step2 = document.querySelector('.step-2');
    step3 = document.querySelector('.step-3');
    field = document.querySelectorAll('.input_control');

    btn_next_1 = document.querySelector('.btn-next-1');
    btn_next_2 = document.querySelector('.btn-next-2');
    btn_back_1 = document.querySelector('.btn-back-1');
    btn_back_2 = document.querySelector('.btn-back-2');

    btn_next_1.addEventListener('click', function(e){
        step1.style.display = 'none';
        step2.style.display = 'flex';
        step3.style.display = 'none';
    })
        btn_next_2.addEventListener('click', function(e){
        step1.style.display = 'none';
        step2.style.display = 'none';
        step3.style.display = 'flex';
    })
        btn_back_2.addEventListener('click', function(e){
        step1.style.display = 'none';
        step2.style.display = 'flex';
        step3.style.display = 'none';
    })
        btn_back_1.addEventListener('click', function(e){
        step1.style.display = 'flex';
        step2.style.display = 'none';
        step3.style.display = 'none';
    })

//    field.forEach(function(el){
//        console.log(el.classList[1]);
//        switch(el.classList[1]){
//            case '1':
//                    step1.append(el);
//                    console.log(el.classList[1]);
//                break;
//            case '2':
//                    step1.append(el);
//                    console.log(el.classList[1]);
//                break;
//            case '3':
//                    step2.append(el);
//                    console.log(el.classList[1]);
//                break;
//            case '4':
//                    step2.append(el);
//                    console.log(el.classList[1]);
//                break;
//            case '5':
//                    step3.append(el);
//                    console.log(el.classList[1]);
//                break;
//            case '6':
//                    step3.append(el);
//                    console.log(el.classList[1]);
//                break;
//        }
//    })
}

function showFileName() {
    let fileName = document.getElementById('id_avatar');
    usersAvatar = document.querySelector('.users-avatar');
        if(fileName.files && fileName.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                usersAvatar.src= e.target.result;
            }
            reader.readAsDataURL(fileName.files[0]);
        }
}