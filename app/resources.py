from flask_restx import Resource, Namespace


ns = Namespace("example", description="Example operations")

@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    
    