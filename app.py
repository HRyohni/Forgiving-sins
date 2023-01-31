from flask import Flask, render_template, request,redirect
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
    if request.method == "POST":
        grijeh = request.form['grijeh']
       
        #BP_Command("insert into login values ( 12 ,'"+username+"','"+password+"');")
        print(grijeh)

   

    return render_template('index.html')


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        BP_Command("insert into login values ( 12 ,'"+username+"','"+password+"');")
        print("done")

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug = True)