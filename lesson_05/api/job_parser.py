from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('team_leader')
parser.add_argument('job')
parser.add_argument('work_size', type=int)
parser.add_argument('collaborators')
parser.add_argument('is_finished', type=bool)
