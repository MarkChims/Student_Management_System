document.addEventListener("DOMContentLoaded", () => {
    const hostelContainer = document.querySelector(".dormitories");
    try{
        fetch(`http://127.0.0.1:8000/staff/dorm-list`, createObject())
            .then((res) => {
            if (!res.ok) throw new Error("Failed to fetch hostels");
            return res.json();
            })
            .then((hostels) => {
                hostels.forEach((hostel) => {
                    const card = document.createElement("div");
                    card.className = "card hostel";

                    const img = document.createElement("img");
                    img.src = hostel.dorm_image;
                    img.className = "hostel-image";
                    card.appendChild(img);

                    const header = document.createElement("div");
                    header.className = "card-header";
                    header.innerHTML = `<h2>${hostel.name}</h2><span class="status">${hostel.status ? "Active" : "Inactive"}</span>`;
                    card.appendChild(header);

                    const info = document.createElement("div");
                    info.className = "info";
                    info.innerHTML = `
                    <span>🏢 <i class="fa fa-level"></i> Capacity: ${hostel.capacity}</span><br>
                    <span>🧍 Occupied: ${hostel.occupied ?? 0}/${hostel.capacity}</span><br>
                    <span>💲 $${hostel.price}</span><br>
                    <span>📍 ${hostel.floors ?? 1} floor${hostel.floors > 1 ? 's' : ''}</span>
                            <div class="tags">
                    <span>WiFi</span>
                    <span>Common Areas</span>
                    <span>Security</span>
                    <span>Canteen</span>
                    </div>
                    `;
                    card.appendChild(info);

                    const tags = document.createElement("div");
                    tags.className = "tags";
                    (hostel.tags || []).forEach(tag => {
                    const tagSpan = document.createElement("span");
                    tagSpan.textContent = tag;
                    tags.appendChild(tagSpan);
                    });
                    card.appendChild(tags);

                    const actions = document.createElement("div");
                    actions.className = "actions-row";
                    const button = document.createElement("button");
                    button.className = "btn";
                    button.textContent = "Allocate Students";
                    button.addEventListener("click", () => {
                        localStorage.setItem("Current-Hostel", hostel.id)
                        window.location.href = "allocate-student.html"
                    })

                    actions.appendChild(button);
                    card.appendChild(actions);

                    hostelContainer.appendChild(card);
                });
                })
                .catch((err) => {
                console.error("Error loading hostels:", err);
                hostelContainer.innerHTML = "<p>Failed to load hostels.</p>";
                });
            }
            catch(error)
            {
                hostelContainer.innerHTML = `<h1>${ error }</h1>`;
            }

    const close = document.querySelector(".emoji")
    const popup = document.querySelector(".popup")
    close.addEventListener("click", () => {
        alert('Hello')
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
