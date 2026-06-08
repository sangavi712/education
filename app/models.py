from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    profile = db.relationship('UserProfile', backref='user', uselist=False)
    progress = db.relationship('UserProgress', backref='user', lazy='dynamic')
    streak = db.relationship('Streak', backref='user', uselist=False)
    knowledge_tree = db.relationship('KnowledgeTree', backref='user', uselist=False)

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age_group = db.Column(db.String(20))
    bio = db.Column(db.Text)
    preferences = db.Column(db.JSON)

class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    meaning = db.Column(db.Text, nullable=False)
    pronunciation = db.Column(db.String(100))
    example = db.Column(db.Text)
    category = db.Column(db.String(50))

class CodingLesson(db.Model):
    __tablename__ = 'coding_lessons'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    language = db.Column(db.String(50))
    content = db.Column(db.Text)
    difficulty = db.Column(db.String(20))

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('coding_lessons.id'))
    type = db.Column(db.String(50))
    question = db.Column(db.Text)
    options = db.Column(db.JSON)
    answer = db.Column(db.String(100))

class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('coding_lessons.id'), nullable=False)
    status = db.Column(db.String(20))
    score = db.Column(db.Integer)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Achievement(db.Model):
    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    xp_reward = db.Column(db.Integer, default=0)
    icon = db.Column(db.String(100))

class Streak(db.Model):
    __tablename__ = 'streaks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    current_streak = db.Column(db.Integer, default=0)
    max_streak = db.Column(db.Integer, default=0)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

class KnowledgeTree(db.Model):
    __tablename__ = 'knowledge_tree'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    current_stage = db.Column(db.String(50), default='Seed')
    total_xp = db.Column(db.Integer, default=0)

class StudyPlan(db.Model):
    __tablename__ = 'study_plans'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date)
    tasks = db.Column(db.JSON)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('vocabulary.id'), nullable=False)
    next_review_date = db.Column(db.Date)
    interval = db.Column(db.Integer, default=1)

class BuddyConversation(db.Model):
    __tablename__ = 'buddy_conversations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text)
    response = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class EmotionLog(db.Model):
    __tablename__ = 'emotion_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    emotion = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
