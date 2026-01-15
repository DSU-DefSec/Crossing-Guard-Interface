const status_element = document.querySelector("#status")
const socket = io()

socket.on("raised", (msg) => {
    status_element.innerHTML = msg
})

socket.on("lowered", (msg) => {
    status_element.innerHTML = msg
})

async function raise() {
    socket.emit("raise")
}

async function lower() {
    socket.emit("lower")
}