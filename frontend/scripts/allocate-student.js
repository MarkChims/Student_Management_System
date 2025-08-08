document.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:8000/staff/student-list", createObject())
        .then(response => {
            if (!response.ok) throw new Error("Failed to load student list");
            return response.json();
        })
        .then(data => {
            const tbody = document.querySelector("tbody");
            data.forEach(student => {
                tbody.appendChild(createTableRow(student));
            });
        })
        .catch(error => {
            console.error("Error fetching students:", error);
        });
});

function createTableRow(student)
{
    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${student.reg_number}</td>
        <td>${student.user.first_name} ${student.user.last_name}</td>
        <td>${student.gender}</td>
        <td><span>${student.level}</span></td>
    `;
    const actionTd = document.createElement("td");
    const allocateBtn = document.createElement("button");
    allocateBtn.className = "danger";
    allocateBtn.textContent = "Allocate";

    allocateBtn.addEventListener("click", (e) => {
        e.preventDefault();
        allocateStudentToDorm(student.id, localStorage.getItem("Current-Hostel"), row, allocateBtn);
    });

    actionTd.appendChild(allocateBtn);
    row.appendChild(actionTd);

    return row;
}

function allocateStudentToDorm(studentId, dormId, row, clickedButton) {
    const accessToken = localStorage.getItem("accessToken")
    fetch("http://127.0.0.1:8000/staff/approve-accomodation", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ accessToken }`
        },
        body: JSON.stringify({
            student: studentId,
            dorm: dormId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
            row.style.display = "none";
        }
    })
    .catch(error => {
        console.error("Allocation error:", error);
        alert("Something went wrong!");
    });
}


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