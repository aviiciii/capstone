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

                const inpt1 = document.createElement("input");
                inpt1.className="form-check-input mt-0";
                inpt1.type="checkbox";
                inpt1.value=student;
                inpt1.ariaLabel="Checkbox for following text input";

                const inpt2 = document.createElement("input");
                inpt2.className="form-control";
                inpt2.type="text";
                inpt2.value=student;
                inpt2.ariaLabel="Disabled input text input with checkbox";
                inpt2.disabled="true";
                inpt2.readOnly="true";

                const innerdiv = document.createElement("div");
                innerdiv.className="input-group-text";
                innerdiv.appendChild(inpt1);



                const div = document.createElement("div");
                div.className="input-group mb-3";
                div.style="width: 80%;"
                div.appendChild(innerdiv);
                div.appendChild(inpt2)


                document.getElementById('students-addable').appendChild(div);
            }
            for (let i = 0; i < present_students.length; i++) {
                const student = present_students[i];

            
                
                const inpt1 = document.createElement("input");
                inpt1.className="form-check-input mt-0";
                inpt1.type="checkbox";
                inpt1.value=student;
                inpt1.ariaLabel="Checkbox for following text input";

                const inpt2 = document.createElement("input");
                inpt2.className="form-control";
                inpt2.type="text";
                inpt2.value=student;
                inpt2.ariaLabel="Disabled input text input with checkbox";
                inpt2.disabled="true";
                inpt2.readOnly="true";

                const innerdiv = document.createElement("div");
                innerdiv.className="input-group-text";
                innerdiv.appendChild(inpt1);



                const div = document.createElement("div");
                div.className="input-group mb-3";
                div.style="width: 80%;"
                div.appendChild(innerdiv);
                div.appendChild(inpt2)



                document.getElementById('students-present').appendChild(div);
            }





        });
            
            
            // result["present_students"].forEach(student => {
            //     console.log(student)
            // document.getElementById('students-addable').innerHTML+=student
            // }
            
            // document.getElementById('studentdetails').innerHTML=result["students"]  
        

    })
})
