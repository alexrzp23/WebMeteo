from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get('nombre', 'Mundo')
    return jsonify({'mensaje': f'Hola, {nombre}!'})

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Por favor, proporciona dos números'}), 400
    return jsonify({'resultado': a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
