from flask import Flask 

#this will connect my postgres database test with python3
import psycopg2

#create the flask app
app = Flask(__app__)

#creating the string which contain our connection info
conn_string = "host='localhost' dbname='test' user='postgres' password='arjunalone18'"

#lets connect it with the database
conn = psycopg2.connect(conn_string) 


#a get request
@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

