from flask import Flask  # import Flask Class from package flask

app = Flask(__name__)  # instance of flask object using our module name as a parameter


@app.route('/')
def hello_world():
    return 'He World!'


# prevent Python scripts from being unintentionally run when they
# are imported into other Python files.
if __name__ == '__main__':
    app.run(debug=True)  # see errors dorectly to the web page
