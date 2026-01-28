const status_element = document.querySelector("#status")
const password_input = document.querySelector("#pass")
const hash = document.querySelector("meta[name='hash']").content
const socket = io()

console.log(hash)

socket.on("raised", (msg) => {
    status_element.innerHTML = msg
})

socket.on("lowered", (msg) => {
    status_element.innerHTML = msg
})

async function raise() {
    sendRequest("/raise")
}

async function lower() {
    sendRequest("/lower")
}

/**
 * 
 * @param {ArrayBuffer} data 
 * @returns {string}
 */
function toHex(data) {
    return Array.from(new Uint8Array(data)).map(b => b.toString(16).padStart(2, '0')).join('')
}

/**
 * 
 * @param {string} msg 
 */
function displayMessage(msg) {
    status_element.innerHTML = msg
}

/**
 * 
 * @param {string} path 
 */
async function sendRequest(path) {
    const new_hash = toHex(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(password_input.value)))
    if (hash == new_hash) {
        const res = await fetch(path, {method: "POST", body: JSON.stringify({password: password_input.value}), headers: {"Content-Type": "application/json"}})
        displayMessage(await res.text())
    }
    else {
        displayMessage("Incorrect password")
    }
}