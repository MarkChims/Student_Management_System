document.addEventListener("DOMContentLoaded", () => {
    const studentsContainer = document.querySelector(".students");
    const add_new_student = document.querySelector("#new-students");

    fetch("http://127.0.0.1:8000/staff/student-list", createObject() )
        .then((res) => {
            if (!res.ok) throw new Error("Failed to fetch hostels");
            return res.json();
        }).then(students => {
            students.map(student => {
                const student_card = document.createElement("div");
                student_card.className = "student-id-card";

                const top_band = document.createElement("div");
                top_band.className = "curved"

                const lower_strip = document.createElement("div");
                lower_strip.className = "down"
                const left_side = document.createElement("div");
                left_side.className = "image"
                const image_profile = document.createElement("img");
                image_profile.src = student.profile_image

                left_side.appendChild(image_profile);

                const right_side = document.createElement("div");
                right_side.className = "student-card-info";
                right_side.innerHTML = "<h3>Student ID Card</h3>"

                const information = document.createElement("div");
                information.className = "details"

                // Information inside the card
                const name = document.createElement("div");
                const level = document.createElement("div");
                const reg_number = document.createElement("div");
                const accomodation = document.createElement("div");

                // assign class
                accomodation.className = "texts";
                name.className = "texts";
                level.className = "texts";
                reg_number.className = "texts";

                name.innerHTML = `
                    <span class="title">Name</span>
                    <span class="title">: ${ student.user.first_name } ${ student.user.last_name }</span>
                `

                accomodation.innerHTML = `
                    <span class="title">Accomodation</span>
                    <span class="title">: Approved</span>
                `

                level.innerHTML = `
                    <span class="title">Form</span>
                    <span class="title">: ${ student.level }</span>
                `

                reg_number.innerHTML = `
                    <span class="title">Reg Number</span>
                    <span class="title">: ${ student.reg_number }</span>
                `

                information.appendChild(name);
                information.appendChild(reg_number);
                information.appendChild(level);
                information.appendChild(accomodation);

                right_side.appendChild(information);


                student_card.appendChild(top_band)
                student_card.appendChild(lower_strip)
                student_card.appendChild(left_side);
                student_card.appendChild(right_side);

                studentsContainer.appendChild(student_card);

            });
        }).catch((error) => {
            studentsContainer.innerHTML = `<h1 class='error'>${ error }</h1>`;
        });

    add_new_student.addEventListener("click", () => {
        window.location.href = "new-student.html"
    })
});

function createObject()
{
    const accessToken = localStorage.getItem("accessToken")
    return {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ accessToken }`
        },
    }
}