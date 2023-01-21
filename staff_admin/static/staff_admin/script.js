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
        .then(result=>{
            console.log(result)
            students = result["students"];
            present_students = result["present_students"];

            for (let i = 0; i < students.length; i++) {
                const student = students[i];
                document.getElementById('students-addable').innerHTML+=student
            }
            for (let i = 0; i < present_students.length; i++) {
                const student = present_students[i];
                document.getElementById('students-present').innerHTML+=student
            }




        });
            
            
            // result["present_students"].forEach(student => {
            //     console.log(student)
            // document.getElementById('students-addable').innerHTML+=student
            // }
            
            // document.getElementById('studentdetails').innerHTML=result["students"]  
        

    })
})
