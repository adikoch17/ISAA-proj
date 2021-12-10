var hght = document.getElementById('hght');
var wdth = document.getElementById('width');
var etilt = document.getElementById('tilt');
var sub = document.getElementById("sub");
var i1 = document.getElementById("i1");
var i2 = document.getElementById("i2");
var img1 = document.getElementById("img1")
var img2 = document.getElementById("img2")

console.log(img1,img2)

hght.oninput = function(){

    etilt.style.transform = `rotateX(${this.value}deg)`;

}

wdth.oninput = () =>{

img1.style.width = `${100/(parseInt(wdth.value)/50)}px`
img2.style.width = `${parseInt(wdth.value)}px`
}

sub.onclick = ()=>{
    fetch('/submit',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({data:`${i1.value},${i2.value}`})
    })
    .then(res=>res.json())
    .then(data => {
        if(data.message=='success'){
            window.alert("CAPTCHA passed")
        }
        else{
            window.alert("CAPTCHA failed" )
        }
    })
}
