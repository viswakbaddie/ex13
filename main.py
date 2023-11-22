from flask import Flask,request,Response
import json
import mysql.connector as mysql
app = Flask(__name__)
con=mysql.connect(host='localhost', user='root',password='password',database='flight_game')
cursor=con.cursor()
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def collect(c):
    query = 'select * from airport;'
    cursor.execute(query)
    data = cursor.fetchall()
    for i in data:
        if i[1] == c:
            d = {"ICAO":c, "name":i[3], "location":i[4]}
    return d


@app.route('/prime_number/<number>')
def prime_number(number):
    bool = prime(int(number))
    response = {'num':number,'result':bool}
    return response

@app.route('/airport/<code>')
def airport(code):
    ans = collect(code)
    return ans
if __name__ == '__main__':
    app.run(debug=True)
