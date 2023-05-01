from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
   return '''
       <form method="post" action="/get_vaccination_status">
           <label for="regno">Enter registration number:</label>
           <input type="text" id="regno" name="regno"><br><br>
           <input type="submit" value="Submit">
       </form>
   '''

@app.route('/get_vaccination_status', methods=['POST'])
def get_vaccination_status():
   regno = request.form['regno']
   mydb = mysql.connector.connect(
       host="db",
       user="root",
       password="root",
       database="db"
   )
   mycursor = mydb.cursor()
   sql = "SELECT Vaccination_Status FROM Students WHERE RegNo = %s"
   val = (regno, )
   mycursor.execute(sql, val)
   result = mycursor.fetchone()
   if result:
       return "Vaccination Status: {}".format(result[0])
   else:
       return "Student not found."

if __name__ == '__main__':
   app.run(host='0.0.0.0')
