document.addEventListener("DOMContentLoaded", function () {

    const sendBtn = document.getElementById("sendBtn");
    const messageInput = document.getElementById("messageInput");

    if (!sendBtn || !messageInput) {
        console.error("HTML elements not found. Check IDs: sendBtn, messageInput");
        return;
    }

    sendBtn.addEventListener("click", function () {

        const message = messageInput.value.trim();

        if (message === "") {
            alert("Please enter a message");
            return;
        }

        fetch("/send", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(res => res.json())
        .then(data => {
            console.log("Response:", data);
            alert(data.reply);
        })
        .catch(err => {
            console.error("Error:", err);
            alert("Server not responding. Check Flask backend.");
        });

    });

});