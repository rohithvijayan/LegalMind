async function signup(){
    console.log("signup clicked")
    email=document.getElementById("email").value
    username=document.getElementById("name").value
    password=document.getElementById("password").value
    rePassword=document.getElementById("re_password").value
    //console.log(`username:${username}\tpassword:${password}\temail:${email}`)
    const user_details={'username':username,'email':email,'password':password,'rePassword':rePassword}
    console.log(user_details)
    const response=await fetch("http://127.0.0.1:8000/api/register/",{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(user_details)
    })
    const responseJson=await response.json()
    console.log(responseJson)
    if(responseJson.message=='Registration successful'){
        // Simulate an HTTP redirect:
        window.location.replace("http://127.0.0.1:8000/");
    }
    else if(responseJson.message=='Registration Failed, Username Already Exists'){
        console.log('Registration Failed, Username Already Exists')
        window.alert('Registration Failed, Username Already Exists')
    }

}