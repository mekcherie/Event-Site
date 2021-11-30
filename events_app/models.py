"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True, unique=True)
    events_attending = db.relationship(
        'Event',
        secondary='guest_event',
        back_populates='guests'
    )

    def __str__(self):
        return f'<Guest: {self.name}>'

    def __repr__(self):
        return f'<Guest: {self.name}>'


class Event_Type(enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    PRODUCT_LAUNCH = 4
    JOB_FAIR = 5


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    guests = db.relationship(
        'Guest',
        secondary='guest_event',
        back_populates='events_attending'
    )
    event_type = db.Column(
      db.Enum(Event_Type),
      default=Event_Type.STUDY,
      nullable=True
    )

    def __str__(self):
        return f'<Event: {self.title}>'

    def __repr__(self):
        return f'<Event: {self.title}>'


guest_event_table = db.Table(
    'guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)