from operator import iadd
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields

from settings import *
from models import *
from ma import *
import bcrypt
# import jwt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)
ma = Marshmallow(app)
# bcrypt = Bcrypt(app)


api = Api(app, version='1.0', title='Consultancy Website API',
        description='An API for Web Application For Concultancy Website')


# Consultancy Website
university_schema = UniversitySchema()
universitys_schema = UniversitySchema(many=True)

study_schema = StudyAreasSchema()
studys_schema = StudyAreasSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

personal_schema = PersonalListSchema()
personals_schema = PersonalListSchema(many=True)

question_schema = QuestionsSchema()
questions_schema = QuestionsSchema(many=True)

answer_schema = AnswersSchema()
answers_schema = AnswersSchema(many=True)

inspiration_schema = InspireSchema()
inspirations_schema = InspireSchema(many=True)


# Study Areas Model
study = api.model("StudyAreas", {
    'UniID': fields.Integer,
    'Fields': fields.String,
    'Undergraduate': fields.Boolean,
    'Postgraduate': fields.Boolean,
})

# User Data Model
user = api.model('User', {
    'FirstName': fields.String('FirstName'),
    'LastName': fields.String,
    'Email': fields.String,
    'Password': fields.String('Secured Password')
})

# Login User Data Model
login = api.model('Login', {
    'Email': fields.String('User Email'),
    'Password': fields.String
})

# University Data Model
uni = api.model("University", {
    'Name': fields.String('Name of the University'),
    'Overview': fields.String,
    'Acronyms': fields.String,
    'Year': fields.DateTime,
    'Motto': fields.String,
    'Website': fields.String,
    'Location': fields.String,
    'Phone': fields.String,
    'Fax': fields.String,
    'Website': fields.String,
    'Location': fields.String,
    'Phone': fields.String,
    'Fax': fields.String,
    'StudentSize': fields.String,
    'AcadamicStaff': fields.String,
    'ControlType': fields.String,
    'Library': fields.Boolean,
    'Housing': fields.Boolean,
    'Region': fields.Boolean,
    'SportFacility': fields.Boolean,
    'FinancialAid': fields.String,
    'SocialMedia': fields.String,
    'Rank': fields.Integer,
    'SocialPassMark': fields.Integer,
    'NaturalPassMArk': fields.Integer,
}) 
# Personal List Data Model
personal = api.model('PersonalList', {
    'UserID': fields.Integer,
    'UniID': fields.Integer
})

# Questions Data Model
questions = api.model('Questions', {
    'UserID': fields.Integer,
    'Questions': fields.String,
    'Date': fields.DateTime
})

#  Answers for the Questions
answers = api.model('Answers', {
    'QuestionID': fields.Integer,
    'Answer': fields.String,
    'Date': fields.DateTime
})





# User Api by Email
@api.route('/api/users/<string:email>')
class userResource(Resource):
    def get(self, email):
        """
        Get user by email
        """
        user = Users.query.filter_by(Email=email).first()
        return user_schema.dump(user)
    
    @api.expect(user)
    @api.response(204, 'User succefully Updated.')
    def put(self, id):
        """
        Updates a user by email
        """
        user = Users.query.filter_by(UserID=id).first()
        if not user:
            return jsonify({'message': "User does not exist"})

        user.FirstName = request.json['FirstName']
        user.LastName = request.json['LastName']
        user.Email = request.json['Email']
        user.Password = request.json['Password']

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user)


# SignUP a User
@api.route('/api/users')
class usersResource(Resource):
    def get(self):
        """
        Get all user
        """
        users = Users.query.all()
        return users_schema.dump(users)

    @api.expect(user)
    def post(self):
        """
        Create a new User
        """
        email = request.json['Email']
        password = request.json['Password']

        user = Users.query.filter_by(Email=email).first()
        if user:
            return jsonify({'message': "The Email Address already exists"})
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = Users(FirstName=request.json['FirstName'],
                        LastName=request.json['LastName'], 
                        Email=request.json['Email'], 
                        Password=hashed)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user)


# Login User
@api.route('/api/users/login')
class UserResource(Resource):
    @api.expect(login)
    def post(self):
        """
        Login a user
        """
        email = request.json['Email']
        password = request.json['Password']

        user = Users.query.filter_by(Email=email).first()
        if not user:
            return jsonify({'message': "User Does not exist"})
        else:
            # if bcrypt.checkpw(password.encode('utf-8'), user.Password):
            if (password==user.Password):
                return user_schema.dump(user)
            else:
                return jsonify({'message': "The Password or Email is Incorrect"})


        # token = jwt.encode({
        #     'user':request.json['email'],
        #     'expiration': datetime.utcnow() + timedelta(minutes=30)
        # },
        #     app.config['SECRET_KEY'])

        # return jsonify({'token': token.decode('utf-8')})

        # user = Users.query.filter()


# University Api
@api.route('/universitys')
class UniversityResource(Resource):
    def get(self):
        """
        Get all universitys
        """
        universitys = University.query.all()
        if not universitys:
            return jsonify({'message': 'There are no Universitys'})
        return universitys_schema.dump(universitys)
    
    @api.expect(uni)
    def post(self):
        """
        Add new university
        """
        
        new_uni = University()
        new_uni.Name = request.json['Name']
        new_uni.Overview = request.json['Overview']
        new_uni.Acronyms = request.json['Acronyms']
        new_uni.Year = request.json['Year']
        new_uni.Motto = request.json['Motto']
        new_uni.Website = request.json['Website']
        new_uni.Location = request.json['Location']
        new_uni.Phone = request.json['Phone']
        new_uni.Fax = request.json['Fax']
        new_uni.StudentSize = request.json['StudentSize']
        new_uni.AcademicStaff = request.json['AcademicStaff']
        new_uni.ControlType = request.json['ControlType']
        new_uni.Library = request.json['Library']
        new_uni.Housing = request.json['Housing']
        new_uni.Region = request.json['Region']
        new_uni.SportFacility = request.json['SportFacility']
        new_uni.FinancialAid = request.json['FinancialAid']
        new_uni.SocialMedia = request.json['SocialMedia']
        new_uni.Rank = request.json['Rank']
        new_uni.SocialPassMArk = request.json['SocialPassMArk']
        new_uni.NaturalPassMArk = request.json['NaturalPassMArk']


        db.session.add(new_uni)
        db.session.commit()

        return university_schema.dump(new_uni)


# University Api with Id
@api.route('/universitys/<int:id>')
class UniversityResource(Resource):
    def get(self, id):
        """
        Get a universitys with id
        """
        uni = []
        universitys = University.query.filter_by(UniID=id).first()
        if not universitys:
            return jsonify({'message': 'There are no Universitys'})
        st_area = StudyAreas.query.filter_by(UniID=id).all()
        uni.append(universitys)
        uni.append(st_area)

        return jsonify(uni)
    
    @api.expect(uni)
    @api.response(204, 'University succefully Updated.')
    def put(self, id):
        new_uni = University.query.filter_by(UniID=id).first()
        if not new_uni:
            return jsonify({'message': "Data not Found"})

        new_uni.Name = request.json['Name']
        new_uni.Overview = request.json['Overview']
        new_uni.Acronyms = request.json['Acronyms']
        new_uni.Year = request.json['Year']
        new_uni.Motto = request.json['Motto']
        new_uni.Website = request.json['Website']
        new_uni.Location = request.json['Location']
        new_uni.Phone = request.json['Phone']
        new_uni.Fax = request.json['Fax']
        new_uni.StudentSize = request.json['StudentSize']
        new_uni.AcademicStaff = request.json['AcademicStaff']
        new_uni.ControlType = request.json['ControlType']
        new_uni.Library = request.json['Library']
        new_uni.Housing = request.json['Housing']
        new_uni.Region = request.json['Region']
        new_uni.SportFacility = request.json['SportFacility']
        new_uni.FinancialAid = request.json['FinancialAid']
        new_uni.SocialMedia = request.json['SocialMedia']
        new_uni.Rank = request.json['Rank']
        new_uni.SocialPassMArk = request.json['SocialPassMArk']
        new_uni.NaturalPassMArk = request.json['NaturalPassMArk']

        db.session.add(new_uni)
        db.session.commit()

        return user_schema.dump(new_uni)



@api.route('/users/<int:id>/list')
class PersonaListResources(Resource):
    def get(self, id):
        """
        Get all personalLists 
        """
        pList = []
        lst = PersonalList.query.filter_by(UserId=id).all()
        if not lst:
            return jsonify({'message': "There are no Lists"})
        for l in lst:
            uni = University.query.filter_by(UniID=l.UniID).first()
            data = {
                'university': uni.Name,
                'Overview': uni.Overview,
                'Rank': uni.Rank
            }
            pList.append(data)       
        return jsonify(pList)


    @api.expect(personal)
    def post(self, id):
        """
        Add to peronalList
        """

        uni = request.json['UniId']
        check = PersonalList.query.filter_by(UniID=uni).first()

        if check:
            return jsonify({'message': "Already Added"})
        new_list = PersonalList()
        new_list.UserId = request.json['UserId']
        new_list.UniId = request.json['UniId']

        db.session.add(new_list)
        db.session.commit()

        return personal_schema.dump(new_list)



@api.route('/questions')
class QuestionsResource(Resource):
    def get(self):
        """
        Get all questions
        """
        qes = Questions.query.all()
        if not qes:
            return jsonify({'message': "There are no questions."})    
        return questions_schema.dumb(qes)
    
    @api.expect(questions)
    def post(self):
        """
        Add a question
        """

        new_ques = Questions()
        new_ques.UserID = request.json['UserID']
        new_ques.Questions = request.json['Questions']
        new_ques.Date = request.json['Date']

        db.session.add(new_ques)
        db.session.commit()

        return question_schema.dump(new_ques)

@api.route('/questions/<int:id>/answer')
class AnswerResource(Resource):
    def get(self, id):
        """
        Get the answers for a question
        """

        ans = Answers.query.filter_by(QuestionID=id).all()
        if not ans:
            return jsonify({'message': "There are no answer for the question"})
        return answers_schema.dump(ans)
    

    @api.expect(answers)
    def post(self, id):
        """
        Add answers for questions by id
        """
        new_ans = Answers()
        new_ans.QuestionID = request.json['QuestionID']
        new_ans.UserID = id
        new_ans.Answer = request.json['Answers']
        new_ans.Date = request.json['Date']

        db.session.add(new_ans)
        db.session.commit()

        return question_schema.dump(new_ans)

@api.route('/inspire')
class InspireResource(Resource):
    def get(self):
        """
        Get Inspiration for Departments
        """
        ins = Inspiration.query.all()
        if not ins:
            return jsonify({'message': "There are no Inspiration"})
        inspirations_schema.dump(ins)

