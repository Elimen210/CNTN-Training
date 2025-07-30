const togg1 = document.getElementById("togg1")
const togg2 = document.getElementById("togg2")


function RevealingTime(type) {
    const signup = document.getElementById("signup")
    const login = document.getElementById("login")

    if (type == 'login') {
        if (!signup.classList.contains('content-none')) {
            signup.classList.add('content-none')
        }

        login.classList.remove('content-none')
    }

    if (type == 'signup') {
        if (!login.classList.contains('content-none')) {
            login.classList.add('content-none')
        }

        signup.classList.remove('content-none')
    }
}

function SearchToggle(type) {
    const row = document.getElementById("search")
    row.classList.toggle("d-none");
}
function UserToggle(type) {
    const signup = document.getElementById("following")
    const login = document.getElementById("follower")

    if (type == 'following') {
        if (!follower.classList.contains('content-none')) {
            follower.classList.add('content-none')
        }

        following.classList.remove('content-none')
    }

    if (type == 'follower') {
        if (!following.classList.contains('content-none')) {
            follower.classList.add('content-none')
        }

        follower.classList.remove('content-none')
    }
}