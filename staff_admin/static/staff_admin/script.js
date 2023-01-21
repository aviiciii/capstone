addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded with JavaScript');

    const button = document.querySelector('#select-class-btn');
    
    button.addEventListener('click', function() {
        console.log('button clicked')
        const class_id = document.querySelector('#class').value;
        let csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

        fetch('class/'+class_id,{
            method:'POST',
            headers:{
                "Content-type":"application/json",
                "X-CSRFToken": csrftoken
            },
        })
        .then(response => response.json())
        .then(result=>
            document.getElementById('studentdetails').innerHTML=result["data"]  
        )
    })
})