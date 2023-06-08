// Get starting likes as a number type
var startingLikes = [9,12,9];

// Increase likes on click
function upLikes(num) {
    startingLikes[num] = startingLikes[num] + 1;

    document.querySelector("#NeilLikes").innerText = startingLikes[0];
    document.querySelector("#NicholeLikes").innerText = startingLikes[1];
    document.querySelector("#JimLikes").innerText = startingLikes[2];
}

