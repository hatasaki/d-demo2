from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    # Get the query parameters
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    # Add the numbers
    result = num1 + num2

    # Return the result as a response
    return str(result)

if __name__ == '__main__':
    # ポート8080でアプリケーションを実行
    app.run(port=8080, host="0.0.0.0")