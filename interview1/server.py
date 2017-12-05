from flask import Flask ,render_template, request,redirect

#this will connect my postgres database test with python3
import psycopg2

#create the flask app
app = Flask(__name__)

#creating the string which contain our connection info
conn_string = "host='localhost' dbname='test' user='postgres' password='arjunalone18'"

#lets connect it with the database
conn = psycopg2.connect(conn_string) 


#a get request
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_location',methods=["POST"])
def post_location():
    pincode = str(request.form["pincode"])
    address = str(request.form["address"])
    city = str(request.form["city"])
    latitude = float(request.form["latitude"])
    longitude = float(request.form["longitude"])
    accuracy = int(request.form["accuracy"])
    curr = conn.cursor()
    try:
        curr.execute("""
        INSERT INTO INDIA VALUES(
            '{}','{}','{}','{}','{}','{}'
        );
        """.format(pincode,address,city,latitude,longitude,accuracy))
        return "Your data has been submitted"
    except:
        return "Sorry primary key already matched"
        
    

if __name__ == '__main__':
    app.run(debug=True)

