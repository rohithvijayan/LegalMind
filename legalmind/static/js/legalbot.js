// Function to toggle between light and dark mode
function toggleTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');

    // Toggle dark mode class on the body
    body.classList.toggle('dark-mode');

    // Save the user's preference in localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        themeToggle.checked = true; // Update the toggle switch state
    } else {
        localStorage.setItem('theme', 'light');
        themeToggle.checked = false; // Update the toggle switch state
    }
}

// Function to load the user's theme preference on page load
function loadTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');

    // Get the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme');

    // Apply the saved theme
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        themeToggle.checked = true;
    } else {
        body.classList.remove('dark-mode');
        themeToggle.checked = false;
    }
}

// Load the theme when the page loads
document.addEventListener('DOMContentLoaded', loadTheme);

// send message as POST

async function sendMessage(){
    const fd=new FormData();
    const msgInput=document.getElementById("user-input")
    const userMessage=msgInput.value
    msgInput.value=""

    const userDiv=document.createElement("div")
    userDiv.setAttribute('class','message user')
    const botDiv=document.createElement('div')
    botDiv.setAttribute('class','message bot')
    const userBubble=document.createElement('div')
    userBubble.setAttribute('class','bubble')
    userBubble.setAttribute("id","userbubble")
    userDiv.appendChild(userBubble)
    botBubble=document.createElement("div")
    botBubble.setAttribute('class','bubble')
    botBubble.setAttribute("id","botbubble")
    userBubble.textContent=userMessage
    const chatDiv=document.getElementById("chat-messages")
    chatDiv.appendChild(userDiv)
    botBubble.textContent="Typing..."
    botDiv.appendChild(botBubble)
    chatDiv.appendChild(botDiv)
    console.log("USER MESSAGE IS : ",userMessage);
    fd.append("usermessage-legalbot",userMessage)
    const response=await fetch("http://127.0.0.1:8000/api/legalbot/",{
        method:"POST",
        body:fd
    });
    const reply=await response.json()
    const botMessage=reply.botReply
    botBubble.textContent=botMessage
    botDiv.appendChild(botBubble)
    chatDiv.appendChild(botDiv)
    console.log("reply from bot:",reply.botReply)
}
