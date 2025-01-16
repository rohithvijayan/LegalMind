async function RagChat(){
    const fd=new FormData();
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
    fd.append("message",userMessage)
    const response=await fetch("http://127.0.0.1:8000/api/ragchat/",{
        method:"POST",
        body:fd
    });
    const reply=await response.json()
    const botMessage=reply.botReply
    botBubble.textContent=botMessage
    chatDiv.appendChild(botBubble)
    console.log("reply from bot:",reply.botReply)
}

async function uploadFile(){
    const uploadInput=document.getElementById("uploadedFile")
    const file=uploadInput.files[0]
    console.log(file)
    const fd=new FormData()
    fd.append("file",file,file.name)
    const repsonse =await fetch("http://127.0.0.1:8000/api/uploadFile/",{
        method:"POST",
        body:fd
    })
    const responseJson=await repsonse.json()
    console.log(responseJson)

}
function clearFile(){
    const uploadInput=document.getElementById("uploadedFile")
    uploadInput.value=''
}

async function Process(){
    const processLoader=document.getElementById("processing_loader")
    processLoader.style.display="block"
    const response=await fetch("http://127.0.0.1:8000/api/process/")
    const responseJson=await response.json()
    processLoader.style.display="none"
    console.log("STATUS OF EMBEDDING:",responseJson)
}

