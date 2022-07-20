
var csrf =document.getElementById('csrf').value

function login(){
    var username=document.getElementById('loginUsername')
    var password=document.getElementById('loginpassword')

    if(username =='' && password==''){
        alert('You must enter both ')
    }

    var data={
        'username' : username,
        'password' : password
    }

    fetch('api/login/',{
        method : 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrf,
        },
        
        body :JSON.stringify(data)
    }).then(result => result.json())
    .then(response =>{
        if(response.status ==200){
            window.location.reload('/')
        }
        else{
            alert(response.message)
        }
    })
}