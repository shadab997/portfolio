from flask import Flask
app = Flask(__name__)

@app.route('/')
def name():
    return "This is Shadab Deployment";
    
    
if __name__ == '__main__':
    app.run(debug = True);