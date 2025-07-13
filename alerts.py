from flask import Flask, render_template, redirect, url_for

alerts = Flask(__name__)

# 홈 화면
@alerts.route('/') 
def alertpage():
    return render_template("alerts.html")

if __name__ == '__main__':
    alerts.run(host='127.0.0.1', port=5500)