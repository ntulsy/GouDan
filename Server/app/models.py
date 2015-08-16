__author__ = 'Siyao'

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    issues_owned = db.relationship('Issue', backref='assigner', lazy='dynamic', foreign_keys='Issue.owner_id')
    issues_assigned = db.relationship('Issue', backref='assignee', lazy='dynamic', foreign_keys='Issue.assignee_id')

    def __repr__(self):
        return '<User %r>' % self.name


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body