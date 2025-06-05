from flask import Flask, render_template, jsonify
from sniffer import start_sniffing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sniff')
def sniff_packets():
    data = start_sniffing(count=10)  # Capture 10 packets
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
# This code sets up a Flask web application that serves a simple HTML page
# and provides an endpoint to sniff network packets. The `sniffer.py` module
# is assumed to contain the packet sniffing logic using Scapy, as shown in the
# provided snippet. The `/sniff` endpoint captures packets and returns them
# as JSON data, which can be used by the frontend to display the captured packets.