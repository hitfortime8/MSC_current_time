from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def Moscow_current_time():
    moscow_zone = ZoneInfo("Europe/Moscow")
    moscow_time = datetime.now(moscow_zone).strftime("%H:%M:%S")
    return render_template('moscow_time.html', time=moscow_time)

if __name__ == '__main__':
    app.run(debug=True)