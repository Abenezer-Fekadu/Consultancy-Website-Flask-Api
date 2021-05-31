from flask_marshmallow import Marshmallow
from models import *

ma = Marshmallow()


# class DinnerSchema(ma.Schema):
#     class Meta:
#         fields = ("Title", "EventDate", "Description", "HostedBy",
#                 "ContactPhone", "Address", "Country", "Latitude", "Longitude")

#         model = Dinner


# class RSVPSchema(ma.Schema):
#     class Meta:
#         fields = ("RsvpID", "DinnerID", "AttendeeName")

#         model = RSVP



# Consultancy Website

class UniversitySchema(ma.Schema):
    class Meta:
        fields = ("Name", "Overview", "Acronym", "Year",
        "Motto", "Location", "Phone", "Website", "Fax")

        model = University


class StudyAreasSchema(ma.Schema):
    class Meta:
        fields = ("UniId", "Fields", "Undergraduate", "Postgraduate",)

        model = StudyAreas

class UsersSchema(ma.Schema):
    class Meta:
        fields = ("FirstName", "LastName", "Email", "Password")

        model = Users


class PersonalListSchema(ma.Schema):
    class Meta:
        fields = ("UserId", "UniId")

        model = PersonalList

class QuestionsSchema(ma.Schema):
    class Meta:
        fields = ("UserID", "Questions", "Date")

        model = Questions

class AnswersSchema(ma.Schema):
    class Meta:
        fields = ("UserID", "QuestionID", "Answer", "Date")

        model = Answers

class InspireSchema(ma.Schema):
    class Meta:
        fields = ("Department","Description")

        model = Inspiration