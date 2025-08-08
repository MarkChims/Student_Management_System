const save_new_student = document.querySelector("#new-sub");

save_new_student.addEventListener("click", (e) => {
    e.preventDefault();

    const selectedPerks  = [];
    const checkboxes = document.querySelectorAll(".perks-container .perk input[type='checkbox']");

    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            const label = checkbox.nextElementSibling.textContent.trim();
            selectedPerks.push(label);
        }
    });

    alert('erwtyuqio')
    const code = document.querySelector("#scode").value;
    const sname = document.querySelector("#sname").value;
    const duration = document.querySelector("#sduration").value;
    const level = document.querySelector("#slevel").value;
    const new_subject =
    {
        "code": code,
        "name": sname,
        "level": level,
        "duration": duration,
        methodologies: JSON.stringify(selectedPerks)
    };

    alert(JSON.stringify(new_subject))

    fetch("http://127.0.0.1:8000/staff/add-subject", createObject(new_subject))
        .then((response) => {
            return response.text();
        })
        .catch((error) => alert(error))
        .finally(() => window.location.href = "subjects.html")

});

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