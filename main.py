from flask import Flask, request, send_file
import qrcode

app = Flask(__name__)


@app.route("/service/qr")
def qrcoder():
    address = request.args.get('payload')
    qr = qrcode.make(address)
    qr.save('code.png')
    return send_file('code.png', mimetype='image/gif')


if __name__ == '__main__':
    app.run(host='172.30.105.99', port=5001)
