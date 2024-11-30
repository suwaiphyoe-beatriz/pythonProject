#no 1
from flask import Flask, jsonify
app = Flask(__name__)

def is_prime(number):

    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

#no 2
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
db_config = {
    "host": "localhost",
    "user": "user1",
    "password": "password",
    "database": "airport"
}

def get_airport_by_icao(icao):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT ICAO_code, name, municipality FROM airports WHERE ICAO_code = %s"
        cursor.execute(query, (icao,))
        airport = cursor.fetchone()
        cursor.close()
        connection.close()
        if airport:
            return {"ICAO": airport[0], "Name": airport[1], "Location": airport[2]}
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airport = get_airport_by_icao(icao.upper())
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
