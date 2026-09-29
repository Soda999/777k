from flask import Flask, render_template, request, jsonify
import mysql.connector
import bcrypt

app = Flask(__name__)

@app.route('/user_register', methods=['POST'])
def user_register():
    req = request.get_json()
    cnx = mysql.connector.connect(
        host="185.114.247.43",
        port=3306,
        database="sch688_vvedenie",
        user="sch688_vvedenie",
        password="Qwerty123")

    name = req['name']
    login = req['email']
    password = bcrypt.hashpw(req['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    date = (name, login, password)
    cur = cnx.cursor()
    cur.execute('INSERT INTO `users`(`username`, `email`, `password_hash`) VALUES (%s, %s, %s)', date)
    cnx.commit()
    cnx.close()

    return 'vse ok'


@app.route('/user_login', methods=['POST'])
def user_login():
    req = request.get_json()

    cnx = mysql.connector.connect(
        host="185.114.247.43",
        port=3306,
        database="sch688_vvedenie",
        user="sch688_vvedenie",
        password="Qwerty123")

    login = req['email']
    password = req['password']

    cur = cnx.cursor(dictionary=True)
    cur.execute('SELECT * FROM `users` WHERE `email` = %s', (login,))
    user = cur.fetchone()
    cnx.close()

    if user is None:
        return jsonify({"status": "error", "message": "Пользователь не найден"}), 401

    if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        return jsonify({"status": "ok", "message": f"Успех! Привет, {user['username']}"})
    else:
        return jsonify({"status": "error", "message": "Неверный пароль"}), 401


@app.route("/")
def registration():
    return render_template('registration.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

app.run(host='0.0.0.0', port=5000)