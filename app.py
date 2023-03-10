from flask import Flask, render_template, request,redirect
from grijehovi import grijesi
import random
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

def pokora(brGrijeha):
    if brGrijeha:
        molitve = ['Oče naša', 'zdravo marijo','slava ocu']
        return "Za pokoru moraš izmoliti: "+ str(random.randint(1,brGrijeha))+" "+str(random.choice(molitve))
    return ""



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
        if 'username' in request.form and 'password' in request.form:
            global username
            global password
            username = request.form['username']
            password = request.form['password']


                #find user
            exsists = BP_DataRow("select * from login where username = '"+ username +"' and passwordd = md5('"+ password +"');")
            if exsists:
                #Get User Data

                return render_template('index.html',action=action,username=username,desc = desc,exsists=exsists)
            else:
                desc="wrong password or username try again."
                return render_template('login.html',action=action,desc=desc)



        if 'grijeh' in request.form:

            count=0
            grijeh = request.form['grijeh']
            for x in grijesi:
                if x.lower() in grijeh.lower():
                    count+=1
                    
            brGrijeha = count
            BP_Command("Update login SET brGrijeha = brGrijeha+ "+str(count)+" , grijesi='"+grijeh+"' where username = '"+ username +"' and passwordd = md5('"+ password +"');")
            Pokora = pokora(brGrijeha)
            return render_template('resault.html',brGrijeha=brGrijeha,Pokora=Pokora)




         
    return render_template('login.html',action=action)

@app.route("/resault", methods = ['GET', 'POST'])
def resault():

    return render_template('resault.html')


if __name__ == "__main__":
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)



