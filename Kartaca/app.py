from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_geek():
    if request.method == 'POST':
        return 'Kartaca Staj 2023'
    return render_template('main.html')

app.debug = True

if __name__ == "__main__":
    app.run(debug=True)