async function Login(){
    username=document.getElementById("name").value
    password=document.getElementById("password").value
    const loginDetails={"username":username,"password":password}
    const response=await fetch("http://127.0.0.1:8000/api/signin/",{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(loginDetails)
    })
    const responseJson=await response.json()
    console.log(responseJson.message)
    if(responseJson.message=='Login successful'){
        window.location.replace("http://127.0.0.1:8000")
    }

}