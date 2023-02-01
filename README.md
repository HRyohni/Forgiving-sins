# Forgiving sins

## Description

This is a page that was made for the purpose of forgiving sins. Any sins, from light to serious, can be confessed here. We also offer a free option to use the station, a monthly option and a premium option witch includes payment.



## main page

Here you can write your sins and they will be forggote

![image-20230201123056270](https://cdn.discordapp.com/attachments/913822641645813772/1070307649943506974/image.png)

## example of paymant on index.html

here you can chose witch payman would you like to use

![img](https://cdn.discordapp.com/attachments/913822641645813772/1070308045143420968/image.png)

## Q & A

if there are any confusion we are providing answers on all your questions

![img](https://cdn.discordapp.com/attachments/913822641645813772/1070308298332590080/image.png)

## index.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/styles/index.css">
    <script src="/static/script/index.js"></script>
    <script src="https://kit.fontawesome.com/342c3b803b.js" crossorigin="anonymous"></script>
    <title>Ispovijed</title>
</head>
<body>

<div style="box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;" class="naslov">

    <br>
    {%if username%}
    <a href="login"><button style = "margin-top: 50px; margin-left: 90%;" class="button-28" role="button"> Sign out</button></a>
    {%else%}
    <a href="login"><button style = "margin-top: 50px; margin-left: 90%;" class="button-28" role="button">Login</button></a>
    {%endif%}


    <h1 style="font-size: 100px; ">Onaj koji oprašta</h1>
    <h3>{{username}}</h3>
     <h3>Ovdje će ti svi grijesi biti oprošteni</h3>
    <form method="POST" >
      <textarea name="grijeh" placeholder="Upiši grijehe" type="text"></textarea>
      <br>
     
        <button  style = "margin-top: 50px; margin-left: 800px; margin-bottom: 50px;"  class="button-28" role="button">Forgive me</button>
      
    </form>

   
    
    <div id="snackbar">Some text some message..</div>
</div>

<div class="main">
  <div class="grid-container">
   <div class="grid-item">
    <div style = "background-color: #E28743;" class="rectangle"></div>

      <div style="padding: 20px;">
      <h4>Free Plan</h4>
      <div class="tekst">
        <p style= "font-size: 16px;"> Free for trying thing out</p>
      </div>

      <button style = "background-color: #E28743; margin-top: 50px;" class="button-28" role="button">Current Plan</button>


    </div>
  </div>

   <div class="grid-item">
    <div style = "background-color: #658D52;" class="rectangle"></div>
      <div style="padding: 20px;">
        <h4>Monthly Plan</h4>
        <div class="tekst">
           <p style= "font-size: 16px;"> For you and your soul, with unlimited confeses and all monthly pro plan features.</p>
        </div>
    </div>
    <button style = "background-color: #658D52; margin-top: 30px;" class="button-28" role="button">Monthly Plan</button>
  </div>

  <div class="grid-item">
    <div style = "background-color: #6652DF;" class="rectangle"></div>
      <div style="padding: 20px;">
        <h4>Premium Plan</h4>
        <div class="tekst">
          <p style= "font-size: 16px;"> For you finding peace with your soul and free pass to heaven all monthly plan features included</p>
        </div>
        <button style = "background-color: #6652DF; margin-top: 50px;" class="button-28" role="button">Premium Plan</button>
     </div>
   </div>
 </div>
</div>



<div style="margin-top: 250px;" class="grid5">
  <div class="grid5-item">
    <br>
  </div>
  <div class="grid5-item">
    <p>Starter</p>
  </div>
  <div class="grid5-item">
    <p>Monthly</p>
  </div>
  <div class="grid5-item">
    <p>Premium</p>
  </div>

  <div  style="height: 50px;" class="grid5-item">
    <br>
  </div>
  <div style="height: 50px;" class="grid5-item">
    <button style = "background-color: #E28743;  color: white; border: none;  " class="button-28" >Current Plan</button>
  </div>
  <div style="height: 50px;" class="grid5-item">
    <button style = "background-color: #549420; color: white; border: none; " class="button-28" role="button">Current Plan</button>
  </div>
  <div style="height: 50px;" class="grid5-item">
    <button style = "background-color: #8952bd; color: white; border: none; " class="button-28" role="button">Current Plan</button>
  </div>

  <div style = "text-align: left;"class="grid5-item">
    Forgiving sins <div class="dropdown">
      <i class="fa-regular fa-circle-question"></i>
  <div class="dropdown-content">
  <div class="desc">Ten sins per day</div>
  </div>
</div>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-check"></i>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-xmark"></i>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-xmark"></i>
  </div>

  <div style = "text-align: left;" class="grid5-item">
    Greater amount of forgiveness of sins

    <div class="dropdown">
      <i class="fa-regular fa-circle-question"></i>
  <div class="dropdown-content">
  <div class="desc">Many more sins per day</div>
  </div>
</div>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-xmark"></i>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-check"></i>
  </div>

  <div class="grid5-item">
    <i class="fa-solid fa-check"></i>
  </div>

  <div style = "text-align: left;" class="grid5-item">
    Direct ticket to Heaven <div class="dropdown">
      <i class="fa-regular fa-circle-question"></i>
  <div class="dropdown-content">
  <div class="desc">You have an apsolute freedom</div>
  </div>
</div>
  </div>
  <div class="grid5-item">
    <i class="fa-solid fa-xmark"></i>
  </div>
  <div class="grid5-item">
    <i class="fa-solid fa-xmark"></i>
  </div>
  <div class="grid5-item">
    <i class="fa-solid fa-check"></i>
  </div>

</div>


<div class="QA">

  <h1 style="text-align: center;">Q&A</h1>



  <button type="button" class="collapsible"><h1>What is this site made for? <i class="fa-solid fa-chevron-down"></i></h1></button>
  <div class="content">
    <p>This site is made to forgive you all your sins.</p>
  </div>
  <hr>

  <button type="button" class="collapsible"><h1>How does this site forgive my sins? <i class="fa-solid fa-chevron-down"></i></h1></button>
  <div class="content">
    <p>Feel free to write in the column whatever and however you want, because this page will automatically recognize which sin it is. If it recognizes your sin/s, the site will forgive you without any problems and along the way you will be able to see how many sins you have confessed so far.</p>
  </div>
  <hr>

  <button type="button" class="collapsible"><h1>What the Monthly plan enables me to do? <i class="fa-solid fa-chevron-down"></i></h1></button>
  <div class="content">
    <p>
The Monthly Plan allows you to forgive more sins than once per day, for each sin you confess you get additional points with which you can reduce your monthly payment and afford some religious items.</p>
  </div>
  <hr>

  <button type="button" class="collapsible"><h1>What the Premium Plan enables me to do? <i class="fa-solid fa-chevron-down"></i></h1></button>
  <div class="content">
    <p>The Premium Plan gives you a direct ticket to heaven, but under the strict obligation that you have to confess all your sins that you have ever committed in your life and at the same time try very hard to sin them again as little as possible..</p>
  </div>
  <hr>

</div>


<div style="margin-top: 250px;" class="bottom">
  <h1 style="background-color: #1d1d1d; color: white;">Sponsors</h1>
<div style="color: white; background-color: #1d1d1d;  border-radius: 10px; font-size: 10px;" class="grid5">

  <h1>koka kola</h1>
  <h1>hubGit</h1>
  <h1>wow</h1>
  <h1>toktik</h1>


</div>
</div>

</body>

</html>



<script>

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}



</script>

```

## We also have a login and register 

With the application, we connected a database into which all new people who want to register will be recorded, and after that the login is transferred, which reads in the database whether this person exists registered in the database.









> ***and of course we have all your data payment and all sins stored in database and number of sins you did.***
>
> ​																			***so***

#                                            dont use this website!









![img](https://cdn.discordapp.com/attachments/913822641645813772/1070308994889039872/image.png)



## This is html code for login and register

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/styles/login.css">
    <title>Login</title>
</head>
<body>

    <div class="main">
      

            <form method="POST">

            <h1>{{action}}</h1>
            <label for="username">Username</label>
            <br>
            <input type="username" placeholder="Username" id="username" name="username">
            <br>
            <label for="password">Lozinka</label>
            <br>
            <input type="password" placeholder="Lozinka" id="password" name="password">
                    
            <button style=" margin-top: 10px; margin-left: 90%;" placeholder="text" type="submit">Done</button>
            <p>{{desc}}</p>
            </form>
            
        </div>
    
</body>
</html>
```



## This is python-flask syntax for database to register users and login them.

```python
from flask import Flask, render_template, request,redirect
from grijehovi import grijesi
import mysql.connector


app = Flask(__name__)


def BP_Command(sql):
    vojska = mysql.connector.connect(host = 'localhost', database = 'grijeh', user = 'root', password = 'root')
    MainKursor = vojska.cursor()
    MainKursor.execute(sql)
    vojska.commit()
    return "Done"

    # Get data row from Database
def BP_DataRow(sql):
    vojska = mysql.connector.connect(host = 'localhost', database = 'grijeh', user = 'root', password = 'root')
    MainKursor = vojska.cursor()
    MainKursor.execute(sql)
    return MainKursor.fetchone()

    # get data ALL from Database
def BP_DataAll(sql):
    vojska =  mysql.connector.connect(host = 'localhost', database = 'grijeh', user = 'root', password = 'root')
    MainKursor = vojska.cursor()
    MainKursor.execute(sql)
    return  MainKursor.fetchall()


    # getting max id


print(BP_DataRow("select max(id) from login;"))
maxid = BP_DataRow("select max(id) from login;")




@app.route("/", methods = ['GET', 'POST'])
def main():
    brGrijeha=0

    if request.method == "POST":
        count=0
        grijeh = request.form['grijeh']
        
        for x in grijesi:
            if x.lower() in grijeh.lower():
                count+=1
                print("f")
        print("found "+ str(count)+ " Grijeha")
        brGrijeha = count
        return render_template('resault.html',brGrijeha=brGrijeha)

        #BP_Command("insert into login values ( 12 ,'"+username+"','"+password+"');")
    
   

    return render_template('index.html',brGrijeha=brGrijeha)


@app.route("/register", methods = ['GET', 'POST'])
def Register():
    action = "Register"

        # Register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        maxID = BP_DataRow("select max(id) from login;")
        BP_Command("insert into login values ( "+str(maxID[0]+1)+  " ,'"+username+"','"+password+"','Standard','',0);")
    return render_template('login.html',action=action)



@app.route("/login", methods = ['GET', 'POST'])
def Login():
    action = "Login"
    desc=""

        # login
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
            #find data
        exsists = BP_DataRow("select * from login where username = '"+ username +"' and passwordd = md5('"+ password +"');")
        if exsists:
            return render_template('index.html',action=action,username=username,desc = desc)
        else:
            desc="wrong password or username try again."
            return render_template('login.html',action=action,desc=desc)                    



         
    return render_template('login.html',action=action)

@app.route("/resault", methods = ['GET', 'POST'])
def resault():

    return render_template('resault.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```