
# app = Flask(__name__)

# def evaluate_expression(expression):
#     try:
#         result = eval(expression)
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route('/evaluate', methods=['POST'])
# def evaluate():
#     data = request.json
#     expression = data.get('expression')
#     if expression is None:
#         return jsonify({'error': 'Expression not provided'}), 400
#     result = evaluate_expression(expression)
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/evaluate', methods=['GET'])
def evaluate():
    query = str(request.args['query'])
    # query = request.args.get('query')
    if query is None:
        return jsonify({'error': 'Query parameter not provided'}), 400

    query = query.replace(' ', '+') 
    try:
        result = eval(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host='192.168.29.92', port=5000, debug=True)

