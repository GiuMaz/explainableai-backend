from sanic import Sanic
from sanic.response import json
from sanic import response
from sanic_cors import CORS, cross_origin

app = Sanic("server")
CORS(app)

# @app.route("/api", methods=["POST"])
# def post_json(request):
#     rule = request.json 
#     return json(rule)

@app.route('/api')
def handle_request(request):
    return response.text('Hello world!')

if __name__ == "__main__":
    app.run(debug=True)
