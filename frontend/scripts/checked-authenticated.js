const accessToken = localStorage.getItem("accessToken");

if (!accessToken) location.href = "login.html"