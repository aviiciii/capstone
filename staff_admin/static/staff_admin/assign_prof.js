addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded with JavaScript');

    const select_class_button = document.querySelector('#select-class-btn');
    
    select_class_button.addEventListener('click', function() {
        console.log('select class button clicked')
        
        const class_id = document.querySelector('#class').value;
        const action = document.querySelector('#action').value;
        let csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

    })
});