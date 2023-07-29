from flask import Flask

app = Flask(__name__)
Courses= ['FCN',
           'COSA',
            'SECURITY CONCEPT',
            'ITIL & DEVOPS',
            'CYBER FORENSIC',
            'COMPLIANCE AUDIT',
             'NDC',
             'PKI']

naam = [ 'Name : Deepanshu Malviya' , 'Courses : PG-DITISS' , 'PRN : 230344223015' , 'Phone Number : 09889656855']

@app.route("/", methods=["GET"])
 
def root():
 return '<h1>Welcome to ITIL exam</h1>'

@app.route("/modules", methods=["GET"])

def get_list():
 return Courses
@app.route("/me", methods=["GET"])

def name():
 return naam

app.run(host="0.0.0.0", port=4000, debug=True)
