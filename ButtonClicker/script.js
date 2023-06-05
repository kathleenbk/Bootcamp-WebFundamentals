// login/logout
function login(elem) {
    console.log(elem.innerText)
    if (elem.innerText == "Login") {
        elem.innerText = "Logout";
    } else {
        elem.innerText = "Login";
    }
};

// remove button
function hide(elem) {
    elem.remove();
}

