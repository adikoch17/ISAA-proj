const express = require('express')
const {spawn} = require('child_process')
const app = express()
const port = 3000

app.use(express.json());
app.use("/web",express.static(__dirname + "/web"));
app.use("/python",express.static(__dirname + "/python"));

app.listen(3000, ()=>{console.log("server is listening")})

var vals = []

app.get('/',(req,res) =>{
    // res.send({"message":"helloo"})
    const python = spawn('python', ['main.py'])
    python.stdout.on('data',(data)=>{
        
        dataToSend = data.toString().trim()
        vals = dataToSend.split(",")
        console.log(vals)
        console.log(`data from python ${dataToSend}`)
    })
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // res.send(dataToSend)
    res.sendFile(__dirname+'/web/index.html')
    })
    
})

app.post('/submit',(req,res)=>{
    data = req.body
    console.log(data)
    var arr = data.data.split(",");
    console.log(arr)
    if (vals[0]==arr[0] && vals[1]==arr[1]){
        res.send({"message":"success"})
    }
    else{
        res.send({"message":"failure"})
    }
    console.log(vals)
    
})