from app.extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("student", back_populates="course")


    def __repr__(self):
        return f"<Course {self.name}>"
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True, nullable=False)
    course_id = db.Column(db.ForeignKey("course_id"))
    
    course = db.relationship("Course", back_populates="students")
    

    def __repr__(self):
        return f"<Student {self.name}>"
