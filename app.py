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
    vojska = mysql.connector.connect(host = 'localhost', database = 'vojska', user = 'root', password = 'root')
    MainKursor = vojska.cursor()
    MainKursor.execute(sql)
    return MainKursor.fetchone()

    # get data ALL from Database
def BP_DataAll(sql):
    vojska =  mysql.connector.connect(host = 'localhost', database = 'vojska', user = 'root', password = 'root')
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


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        BP_Command("insert into login values ( 12 ,'"+username+"','"+password+"');")
        print("done")

    return render_template('login.html')


@app.route("/resault", methods = ['GET', 'POST'])
def resault():

    return render_template('resault.html')


if __name__ == "__main__":
    app.run(debug = True)