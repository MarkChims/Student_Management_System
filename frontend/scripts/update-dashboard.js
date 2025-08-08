// Replace with your real API endpoint URL
const apiUrl = "http://127.0.0.1:8000/staff/studentsstats";

// You can add month/year query params if needed, for example:
// const month = new Date().getMonth() + 1; // JS month is 0-based
// const year = new Date().getFullYear();
// const apiUrl = `/staff/dashboardstats?month=${month}&year=${year}`;

fetch(apiUrl)
.then(response => response.json())
.then(data => {
    // Update the numbers in the HTML with API data
    document.querySelector(".stats-strip").innerHTML = 
    `
        <div class="dash-card blue">
            <i class="fa fa-male"></i>
            <h1 class="number">${ data.male_count }</h1>
            <span class="title">Male</span>
        </div>

        <div class="dash-card red">
            <i class="fa fa-female"></i>
            <h1 class="number">${ data.female_count }</h1>
            <span class="title">Females</span>
        </div>

        <div class="dash-card green">
            <i class="fa fa-graduation-cap"></i>
            <h1 class="number">${ data.total_count }</h1>
            <span class="title">Total Students</span>
        </div>
        <h1>Enrolled Students Students</h1>
    `

    document.getElementById("month-residences").textContent = data.month_residences;
    document.getElementById("students-with-subjects").textContent = data.students_with_subjects;
    document.getElementById("total-students").textContent = data.total_students;
})
.catch(error => {
    console.error("Error fetching dashboard stats:", error);
});