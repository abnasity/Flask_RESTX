from app.extensions import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    students = db.relationship("Student", back_populates="course")

    def __repr__(self):
        return f"<Course {self.name}>"

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    course = db.relationship("Course", back_populates="students")

    def __repr__(self):
        return f"<Student {self.name}>"
