from flask import Flask
import sys
import optparse
import time
#import psycopg2

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():
    # take them from secrets and config file
    #connection = psycopg2.connect(user = "myadmin",
     #                             password = "admin1234",
      #                            host = "db-service",
       #                           port = "5432",
        #                          database = "mydb")
    #cursor = connection.cursor()                                  
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    return "Hola mario"
    #return record

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python webapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(
        host='0.0.0.0', 
        port=int(args.port), 
        debug=True)