from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([
        {"id": 1001, "product_id": 101, "user_id": 1},
        {"id": 1002, "product_id": 102, "user_id": 2}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
