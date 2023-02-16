const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "xavier" && password === "error404") {
        window.location = "home.html"
    } else if(username === "natalie" && password === "Newyear_2023") {
        window.location = "home.html"

    } else {
        loginErrorMsg.style.opacity = 1;
    }
})