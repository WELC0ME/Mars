from api.users_parser import parser
from flask_restful import abort, Resource
from flask import jsonify
from data.jobs import Jobs
from data import db_session


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        abort(404, message=f"Job {job_id} not found")


class JobResource(Resource):

    def get(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        if not job:
            return jsonify({'error': 'Not found'})
        return jsonify({
            'jobs': job.to_dict(only=(
                'id',
                'team_leader',
                'job',
                'work_size',
                'collaborators',
                'is_finished',
            )),
        })

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == args['id']).first()
        if not job:
            return jsonify({'error': 'Bad request'})
        job.team_leader = args.get('team_leader', job.team_leader)
        job.job = args.get('job', job.job)
        job.work_size = args.get('work_size', job.work_size)
        job.collaborators = args.get('collaborators', job.collaborators)
        job.is_finished = args.get('is_finished', job.is_finished)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):

    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify({
            'jobs': [item.to_dict(only=(
                'id',
                'team_leader',
                'job',
                'work_size',
                'collaborators',
                'is_finished',
            )) for item in jobs],
        })

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(args['id'])
        if job:
            return jsonify({'error': 'Id already exists'})
        if not all(key in args.keys() for key in [
            'id',
            'team_leader',
            'job',
            'work_size',
            'collaborators',
            'is_finished'
        ]):
            return jsonify({'error': 'Bad request'})
        job = Jobs(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
