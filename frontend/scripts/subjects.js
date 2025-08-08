document.addEventListener("DOMContentLoaded", () => {
    const accessToken = localStorage.getItem("accessToken");
    const subjectContainer = document.querySelector(".subjects");

    fetch("http://127.0.0.1:8000/staff/subject-list", createObject())
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            response.json().then(subjects => {
                subjects.forEach(subject => {
                    const card = document.createElement("div");
                    card.className = "subject-card";

                    card.innerHTML = `
                        <div class="title-info">
                        <h2>${subject.name}</h2>
                        <span class="status">On-Going</span>
                        </div>
                        <div class="perks">
                        <span class="capacity"><i class="fa fa-address-card"></i> Class Enrollment: 45 students</span>
                        <span class="program"><i class="fa fa-clock-o"></i> Duration: ${subject.duration}</span>
                        <span class="level-access"><i class="fa fa-line-chart"></i> Level: ${subject.level}</span>
                        </div>
                        <div class="composition">
                        ${JSON.parse(subject.methodologies).map(c => `<span class="components">${c}</span>`).join('')}
                        </div>
                    `;

                    const button = document.createElement("button");
                    button.className = "view"
                    button.textContent = location.href.includes("students") ? "Enroll" : "View"
                    button.addEventListener("click", () => {
                        fetch(
                            "http://127.0.0.1:8000/student/register/",
                            {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/json",
                                    "Authorization": `Bearer ${ accessToken }`
                                },
                                body: JSON.stringify(
                                    {
                                        subject: subject.id,
                                        student: 2
                                    }
                                )
                            }
                        )
                        .then(response => {
                            if (!response.ok) throw new Error("Failed")
                            return response.json();
                        }).catch((error) => alert(error));
                    })
                    card.appendChild(button);

                    subjectContainer.appendChild(card);
                });
            })
        })
        .catch(error => {
            console.error("Error fetching subjects:", error);
            subjectContainer.innerHTML = "<p>Failed to load subjects.</p>";
        }).finally(() => {
            if (location.href.includes("student"))
            {
                document.querySelector(".capacity").style.display = "none";
                document.querySelector(".level-access").style.display = "none";
            }
        });
    })

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