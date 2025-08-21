from flask import Flask
from flask import render_template
from flask import request
from dotenv import load_dotenv
from flask import redirect

load_dotenv()  # take environment variables


app = Flask(__name__)

@app.route("/")
def hello_world():
    a="""   <!DOCTYPE html>
  <head>
    <script>
       //var gender =document.getElementById('hobby').value
 //var checkedValue = document.querySelector('.messageCheckbox:checked').value;
// console.log(checkedValue)
    </script>
    <script>
  window.addEventListener('load',function(){
    document.getElementById("demo").innerText = "Hello World";//changes the inner text of demo to lower world
   
  });

</script>
  </head>
<body>
<h2>My First JavaScript</h2>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()"><!--prints date on demo when button is clicked -->
Click me to display Date and Time.</button>

<p id="demo"></p>
<h2>HTML Forms</h2>

<button type="button" onclick='document.getElementById("demo").innerHTML = "Hello JavaScript!"'>Click Me!</button>
<button type="button" id="buttontest">test me !</button>

<script>
document.write(5 + 6);
let x, y, z;    // Statement 1
x = 5;          // Statement 2
y = 16;          // Statement 3
z = x + y;      // Statement 4
document.writeln(z)//print on screen value of z
document.getElementById("demo").innerHTML = "John" + " "  + "Doe";//joining two words

x = 5 + 6;//add 5+6
y = x * 10; //multiply x*10
document.writeln(y)
// x = 6;   I will NOT be executed
var h = "John Doe";

var h= 0;
const PI = 3.141592653589793;
//PI = 3.14;      // This will give an error
//PI = PI + 10;   // This will also give an error
// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];

// You can change an element:
cars[0] = "Toyota";

// You can add an element:
cars.push("Audi");
//document.print(cars[0])
document.getElementById("demo").innerHTML = cars;
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};
//alert("how are you")
// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson"
document.getElementById("demo").innerHTML = "Car owner is " + car.owner; 
let p = 5;//declares an intager p asigns it 5
let q = 2;
let r= p % q; //gives the remainder
document.writeln(r)//prints value of r on to the page 
const date = new Date("2022-03-25");
document.writeln(date)
// Function to compute the product of p1 and p2
function myFunction(p1, p2) {//heaad function body taking in two parameters p1 p2
  return p1 * p2;//fuction body that retuns product of p1 p2
}
var answer=myFunction(p,q)//calling/executing/running the function caled my function and passing p q as parametrs 
document.writeln(answer)//displaying the results of calculation 
var hobby='S'

 
switch(hobby) {//head of switch funtion/switch block takes hobby as a condition

  case 't':case 'T'://takes for condition t with a lower case or upper
   console.log ("travell to dubai")//printsto console 
    // code block
    break;
  case 's':case 'S'://checks for condition s 
   console.log ("swim in zanzibar")//print result of condition s
    // code block
    break;
  default:
    console.log('choose either s/t')
    // code block
}
//document.readln
var day = 4;
switch (day) {
  case 6:
   console.log("Today is Saturday");
    break;
  case 7:
   console.log("Today is Sunday");
    break;//exits the switch case block 
  default:
    console.log("Looking forward to the Weekend");
}
// Outputs "Looking forward to the Weekend"
function updateHTML(elmId, value) {
  var elem = document.getElementById(elmId);
  if(typeof elem !== 'undefined' && elem !== null) {
    elem.innerHTML = value;
  }
}

window.addEventListener('load',function(){
  buttontest=document.getElementById("buttontest")
console.log(buttontest)
const lname=document.getElementById("lname").value
//let myname=document.getElementById("firstname ").value;
const password=document.getElementById("password").value
const message=document.getElementById("message").innerHTML
//const select=document.getElementById("select")
const dob=document.getElementById("dob")
const appname=document.getElementById ("appname").innerHTML
const applicationweek=document.getElementById("applicationweek")
const idnumber=document.getElementById("idnumber").value
const elem=document.getElementById("myfile").value
const career=document.getElementById("career").value
const monthSelect = document.querySelector("#month");
const cvuploads=document.getElementById("cvuploads").value
const photo=document.getElementById("photo")
const colourpick=document.getElementById("colourpick").value
//elem.addEventListener("change", () => {
var e = document.getElementById("ddlViewBy");
var value = e.value;
var text = e.options[e.selectedIndex].text;
 // if (elem.files.length == 1) {
  
  // }
//});
//const fname=x
   //console.log(fname)

   //var fullname=fname+" "+lname

//console.log(lname)
buttontest.addEventListener("click",function(){
  console.log(lname)
  console.log(password)
 // console.log (myname)
  console.log(message)
  //console.log(select)
  console.log(dob)
console.log (appname)
console.log(applicationweek)
console.log(idnumber)
console.log(myfile)
console.log(career)
console.log (monthSelect)
console.log(cvuploads)
console.log(photo)
console.log(colourpick)
console.log (e)
console.log (value)
console.log (text)
 // console.log("File selected: ", elem.files[0]);
})


  });
  function myFunctionselect() {
  var x = document.getElementById("ddlViewBy").value;
  document.getElementById("demo").innerHTML = "You selected: " + x;
}


</script>
p>When you select a new car, a function is triggered which outputs the value of the selected car.</p>

<p id="demo"></p>

<form action="action_page.php">
  <label for="lfname">First name:</label><br>
  <input type="text" id="firstname" name="fname" value="" ><br>
  <label for="llname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value=><br><br>
	<input type="text"id="password"value=""><br><br>
  <textarea name="message" id="message">ttttt</textarea><br><br>
  <input type="radio" id="gender" name="gender" value="F"><label id="genderf">female</label>

  <input type="radio"id="gender" name="gender"VALUE="M"><label> id="genderm">male</label><br><br>
  <select id="title">
  	<option>Mr.</option>
    <option>Mrs.</option>
    <option>Dr.</option>
    </select><br><br>
 
  <input type="checkbox"  class ='messageCheckbox'name="hobby"value="s"><label>swimming</label>
  <input type="checkbox" name="hobby" value="t"><label>travelling</label><br><br>
   <input type="submit" value="save record">
  <button>send</button>
  
    <input type="button">
    <input type="checkbox">
   colour <input type="color"id="colourpick">
    <input type="date" id="dob">
    <input type="datetime-local" id="applicationdate">
    <input type="email">
    <input type="file" id="myfile">
    <input type="hidden" id="appname" value="facebook">
   photo <input type="image"id="photo">
    <input type="month">
    <input type="number" id="idnumber">
    <input type="password">
    <input type="radio" id="career" value="medlab">
    <input type="range">
    <input type="reset">
    <input type="search"id="cvuploads">
    <input type="submit">
    <input type="tel"id="telephone">
    <input type="text">
    <input type="time"id="event_time">
    <input type="url">
    <input type="week"id="applicationweek">
    <select id="ddlViewBy" onchange="myFunctionselect()">
  <option value="1">test1</option>
  <option value="2" >test2</option>
  <option value="3">test3</option>
</select>

</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>


</body>
</html>


"""
    return a

@app.route("/home")
def index():
    return render_template("/index.html")
@app.route("/nursing/specialties")
def specialties():
    return ("pediatrics")
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('index.html', name=user)
import mysql.connector
#INSERT INTO `staff` (`id`, `fullnames`, `dateofbirth`, `specialty`) VALUES (NULL, 'Joyce Wairimu', '2025-05-09', 'othopidic ');
#INSERT INTO `staff` (`id`, `fullnames`, `dateofbirth`, `specialty`) VALUES (NULL, 'Sandra gesare', '2025-05-14', 'oncology nursing
@app.route("/nursing/nurses")
def nurses():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="nursesheduledb")
  print(mydb)
  mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
 # print(x)


  
  mycursor.execute("SELECT * FROM staff WHERE fullnames LIKE 'a%';")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
  return (x)
@app.route ("/list/cars")
def list():
   mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="nursesheduledb")
   
   print(mydb)
   mycursor = mydb.cursor()
   mycursor.execute("SELECT staff.id, staff.fullnames, dutyroster.Shift_number FROM staff INNER JOIN dutyroster ON staff.id=dutyroster.id;")
   cars=["Ford", "Volvo", "BMW"]
   myresult = mycursor.fetchall()

   
  # results=mycursor
   y=len(cars)
   print (y)
   for x in cars:
    print (x)
  

   

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
 # print(x)

  
 
#cars[0]="marcedes"
 # x = cars[0]
#print(cars[0])
 # cars.pop(2)
#print(cars[0])
 # cars.remove("Volvo")
 
    return render_template('list.html', cars=cars,results=myresult,name="mwebi")
   
@app.route("/list/form", methods=['GET'])
def  formaddstaff():
   print ("adding a record")
   fullname=""
   dateofbirth=""
   specialty=""
  # fullname= request.form['fullname']
   #dateofbirth=request.form("fullname")
   #specialty=request.form("fullnmaes")
   #print(fullname)
   return render_template('addrecord.html')
  
   #INSERT INTO `dutyroster`(`id`, `Shift_number`, `Staff_id`, `shift-id`, `Comments`, `Created_At`, `Updated_At`) VALUES( 4,'shift3
#','4','2',' move bed 4 to ward 3 ','','');

@app.route("/list/add", methods=['POST'])
def addstaff():
   print ("adding a record")
   fullname=""
   dateofbirth=""
   specialty=""
   fullname= request.form['fullname']
   #dateofbirth=request.form("fullname")
   #specialty=request.form("fullnmaes")
   print(fullname)
   return fullname
   #return render_template('addrecord.html')

   from flask import url_for

@app.route('/')
def home2():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

#from flask import Flask, redirect

#app = Flask(__name__)

@app.route('/current_location')
def currentlocation():
   # return redirect('/submit_data')
  return render_template('addrecord.html')
  

@app.route('/new_location')
def new_location():
    return 'You have been redirected from current to new!'

@app.route('/submit_data', methods=['POST','GET'])
def submit_data():
    data = request.form['fullname']
    print (data)
    return redirect("/new_location")
        # ...
    # allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>''' 
           



