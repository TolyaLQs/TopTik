window.onload = function(){
    step1 = document.querySelector('.step-1');
    step2 = document.querySelector('.step-2');
    step3 = document.querySelector('.step-3');
    field = document.querySelectorAll('.input_control');

    field.forEach(function(el){
        console.log(el.classList[1]);
        switch(el.classList[1]){
            case '1':
                    step1.append(el);
                    console.log(el.classList[1]);
                break;
            case '2':
                    step1.append(el);
                    console.log(el.classList[1]);
                break;
            case '3':
                    step2.append(el);
                    console.log(el.classList[1]);
                break;
            case '4':
                    step2.append(el);
                    console.log(el.classList[1]);
                break;
            case '5':
                    step3.append(el);
                    console.log(el.classList[1]);
                break;
            case '6':
                    step3.append(el);
                    console.log(el.classList[1]);
                break;
        }
    })
}