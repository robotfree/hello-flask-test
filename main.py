from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])

def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)

@app.route('/health', methods=['GET'])
def health():
	if(request.method == 'GET'):
		data = {"data": "OK"}
		return jsonify(data)

@app.route('/', methods=['GET'])
def root():
	if(request.method == 'GET'):
		data = {"data": "/"}
		return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
