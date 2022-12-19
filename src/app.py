import socket
from flask import Flask,jsonify,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, YadavJi</p>"

@app.route("/health")
def health():
    return jsonify (
        status = "up"
    )

@app.route("/application")
def application():
    host,ip = clusterdetails()
    return render_template ("index.html", index_hostname = host,index_ip = ip)

# function to fetch cluster details
def clusterdetails():
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name,host_ip


print("hello SMY")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)