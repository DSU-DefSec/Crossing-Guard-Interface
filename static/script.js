const status_element = document.querySelector("#status")
const socket = io()

socket.on("connect", () => {
    console.log("connected")
})

socket.on("raise", () => {
    status_element.innerHTML = "raised"
})

socket.on("lower", () => {
    status_element.innerHTML = "lowered"
})

async function raise() {
    const res = await fetch("/raise")
    status_element.innerHTML = await res.text()
}

async function lower() {
    const res = await fetch("/lower")
    status_element.innerHTML = await res.text()
}