const allocate_room = document.querySelector("#checkbox");
allocate_room.addEventListener("click", () => {
    if (allocate_room.checked)
    {
        fetch("http://127.0.0.1:8000/staff/room-list")
            .then()
    }
})

const save_new_student = document.querySelector(".button");

save_new_student.addEventListener("click", (e) => {
    e.preventDefault();
    const fname = document.querySelector("#fname").value;
    const lname = document.querySelector("#lname").value;
    const gender = document.querySelector("#gender").value;
    const contact = document.querySelector("#email").value;
    const image = document.querySelector("#profile-image").value;
    const level = document.querySelector("#level").value;
    const allocate = allocate_room.checked;
    const reg_number = generateRandomID()
    const new_student =
    {
        user: {
            username: reg_number,
            first_name: fname,
            last_name: lname,
            email: contact,
            password: reg_number
        },
        reg_number: reg_number,
        gender: gender,
        // profile_image: image,
        level: parseInt(level)
    };

    fetch("http://127.0.0.1:8000/staff/add-student", createObject(new_student))
        .then((response) => {
            response.text().then((text) => alert(text))
        })
        .then(data => `New Student Successfully Created`)
        .catch((error) => alert(error))
        .finally(() =>{
            if (allocate)
            {

                fetch("http://127.0.0.1:8000/staff/",createObject() )
            }
            window.location.href = "students.html"
        });


});




function generateRandomID()
{
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const year = (new Date().getFullYear() % 100) * 10;
    const random_3_digit_code = Math.floor(Math.random() * 1000);
    const random_letter = letters.charAt(Math.floor(Math.random() * 26));

    return `H${ year }${ random_3_digit_code }${ random_letter }`;

}

function createObject(student)
{
    const accessToken = localStorage.getItem("accessToken")
    return {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ accessToken }`
        },
        body: JSON.stringify(student)
    }
}