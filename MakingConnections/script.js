function nameChange() {
    if (username.innerText === "Jane Doe"){
    username.innerText = "Katie Kavanagh";
    } else { username.innerText = "Jane Doe";}
};

function removeRequest(id) {
    document.querySelector(id).remove();
}