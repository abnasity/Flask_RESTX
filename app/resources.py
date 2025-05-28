from flask_restx import Resource, Namespace
from .extensions import db
from .models import Course, Student
from .api_models import course_model, student_model, course_input_model, student_input_model

ns = Namespace("example", description="Example operations")

@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    

@ns.route("/courses")
class CourseAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def post(self):
        print(ns.payload)
        course = Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course, 201
    
@ns.route("/courses/<int:id>")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        course = Course.query.filter_by(id=id).first()
        return course
    
    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def put(self, id):
        course = Course.query.filter_by(id=id).first()
        course.name = ns.payload["name"]
        db.session.commit()
        return course
    
    def delete(self, id):
        course = Course.query.filter_by(id=id).first()
        db.session.delete(course)
        db.session.commit()
        return {}, 204


@ns.route("/students")
class StudentsAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload["name"], course_id=ns.payload["course_id"])
       
        db.session.add(student)
        db.session.commit()
        return student, 201
    
@ns.route("/students/<int:id>")
class studentAPI(Resource):
    @ns.marshal_with(student_model)
    def get(self, id):
        student = Student.query.filter_by(id=id).first()
        return student
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def put(self, id):
        student = Student.query.filter_by(id=id).first()
        student.name = ns.payload["name"]
        student.course_id = ns.payload["course_id"]
        db.session.commit()
        return student
    
    def delete(self, id):
        student = Student.query.filter_by(id=id).first()
        db.session.delete(student)
        db.session.commit()
        return {}, 204