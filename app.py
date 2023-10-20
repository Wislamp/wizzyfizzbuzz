from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def fizzbuzz():
    fizz = [number for number in range(1, 101) if number % 3 == 0]
    buzz = [number for number in range(1, 101) if number % 5 == 0]
    fizzbuzz = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
    return render_template("index.html", fizz=fizz, buzz=buzz, fizzbuzz=fizzbuzz)


