async function RagChat(){
    const msgInput=document.getElementById("user-msg-input")
    const userMessage=msgInput.value
    const userBubble=document.createElement("div")
    userBubble.setAttribute('id','chat-bubble-user')
    const botBubble=document.createElement('div')
    botBubble.setAttribute('id','chat-bubble-bot')
    userBubble.textContent=userMessage
    const chatDiv=document.getElementById("chat")
    chatDiv.appendChild(userBubble)
    console.log("USER MESSAGE IS : ",userMessage);
    msgInput.value=""
    const response=await fetch("http://127.0.0.1:8000/api/ragchat/",{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            message:userMessage
        })
    })
    const reply=await response.json()
    const botMessage=reply.botReply
    botBubble.textContent=botMessage
    chatDiv.appendChild(botBubble)
    console.log("reply from bot:",reply.botReply)
}