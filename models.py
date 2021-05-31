from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# class Dinner(db.Model):
#     __tablename__ = "dinners"
#     DinnerID = db.Column(db.Integer, primary_key=True)
#     Title = db.Column(db.String, nullable=False)
#     EventDate = db.Column(db.DateTime, nullable=False)
#     Description = db.Column(db.String, nullable=True)
#     HostedBy = db.Column(db.String, nullable=False)
#     ContactPhone = db.Column(db.String, nullable=True)
#     Address = db.Column(db.String, nullable=False)
#     Country = db.Column(db.String, nullable=False)
#     Latitude = db.Column(db.Float, nullable=False)
#     Longitude = db.Column(db.Float, nullable=False)


# class RSVP(db.Model):
#     __tablename__ = "rsvps"
#     RsvpID = db.Column(db.Integer, primary_key=True)
#     DinnerID = db.Column(db.Integer, db.ForeignKey(
#         "dinners.DinnerID"), nullable=False)
#     AttendeeName = db.Column(db.String, nullable=False)

class University(db.Model):
    __tablename__ = "university"
    UniID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Acronyms = db.Column(db.String, nullable=False)
    Motto = db.Column(db.String, nullable=False)
    Overview = db.Column(db.String, nullable=False)
    Website = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)
    Location = db.Column(db.String, nullable=False)
    Phone = db.Column(db.String, nullable=False)
    Fax = db.Column(db.String, nullable=False)
    Year = db.Column(db.DateTime, nullable=False)
    StudentSize = db.Column(db.String, nullable=False)
    AcademicStaff = db.Column(db.String, nullable=False)
    ControlType = db.Column(db.String, nullable=False)
    Library = db.Column(db.Boolean, nullable=False)
    Housing = db.Column(db.Boolean, nullable=False)
    SportFacility = db.Column(db.Boolean, nullable=False)
    FinancialAid = db.Column(db.Boolean, nullable=False)
    SocialMedia = db.Column(db.String, nullable=False)
    Rank = db.Column(db.Integer, nullable=False)
    SocialPassMArk = db.Column(db.Integer, nullable=False)
    NaturalPassMArk = db.Column(db.Integer, nullable=False)

class StudyAreas(db.Model):
    __tablename__ = "study_areas"
    StudyID = db.Column(db.Integer, primary_key=True)
    UniID = db.Column(db.Integer, db.ForeignKey("university.UniID"), nullable=False)
    Fields = db.Column(db.String, nullable=False)
    Undergraduate = db.Column(db.Boolean, nullable=False)
    Postgraduate = db.Column(db.Boolean, nullable=False)

class Users(db.Model):
    __tablename__ = "users"
    UserID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String, nullable=False)
    LastName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)

class PersonalList(db.Model):
    __tablename__ = "personal_list"
    PersonalID = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey("users.UserID"), nullable=False)
    UniId = db.Column(db.Integer, db.ForeignKey("university.UniID"), nullable=False)

class Questions(db.Model):
    __tablename__ = "questions"
    QuestionID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey("users.UserID"),nullable=False)
    Questions = db.Column(db.Text, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)


class Answers(db.Model):
    __tablename__ = "answers"
    AnswerID = db.Column(db.Integer, primary_key=True)
    QuestionID = db.Column(db.Integer, db.ForeignKey("questions.QuestionID"), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey("users.UserID"))
    Answer = db.Column(db.Text, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)


class Inspiration(db.Model):
    __tablename__ = "inspiration"
    InspireID = db.Column(db.Integer, primary_key=True)
    Department = db.Column(db.String, nullable=False)
    Description = db.Column(db.Text, nullable=False)