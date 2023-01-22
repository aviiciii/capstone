addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded with JavaScript');

    const button = document.querySelector('#select-class-btn');
    
    button.addEventListener('click', function() {
        console.log('button clicked')
        
        const class_id = document.querySelector('#class').value;
        const action = document.querySelector('#action').value;
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

            if (action === "add") {
                console.log("add")

                for (let i = 0; i < students.length; i++) {
                    const student = students[i];

                    const inpt1 = document.createElement("input");
                    inpt1.className="form-check-input mt-0";
                    inpt1.type="checkbox";
                    inpt1.value=student;
                    inpt1.name="students";
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
                    div.style="width: 30%;"
                    div.appendChild(innerdiv);
                    div.appendChild(inpt2)


                    document.getElementById('students-addable').appendChild(div);


                }

                if (students.length === 0) {
                    document.getElementById('students-addable').innerHTML = "No students present";
                    document.getElementById('add-students-btn').disabled = true;

                }

                // add class_id to form
                document.getElementById('class-id-add-form').value = class_id;

                // set display to block
                document.getElementById('form-add-students').style.display = "block";
                document.getElementById('form-remove-students').style.display = "none";

            } else {
                console.log("remove")
                for (let i = 0; i < present_students.length; i++) {
                    const student = present_students[i];

                
                    
                    const inpt1 = document.createElement("input");
                    inpt1.className="form-check-input mt-0";
                    inpt1.type="checkbox";
                    inpt1.value=student;
                    inpt1.name="students";
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
                    div.style="width: 30%;"
                    div.appendChild(innerdiv);
                    div.appendChild(inpt2)



                    document.getElementById('students-present').appendChild(div);
                }

                // add class_id to form
                document.getElementById('class-id-remove-form').value = class_id;

                if (present_students.length === 0) {
                    document.getElementById('students-present').innerHTML = "No students present";
                    document.getElementById('remove-students-btn').disabled = true;
                }

                // set display to block
                document.getElementById('form-remove-students').style.display = "block";
                document.getElementById('form-add-students').style.display = "none";
            }
            document.getElementById('select-class-btn').disabled = true;
            // set display to block

            document.getElementById('refresh-class-btn').style.display = "block";




        });
            
            
            // result["present_students"].forEach(student => {
            //     console.log(student)
            // document.getElementById('students-addable').innerHTML+=student
            // }
            
            // document.getElementById('studentdetails').innerHTML=result["students"]  
        

    })
})
