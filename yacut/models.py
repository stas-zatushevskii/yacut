from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(16), nullable=False)
    original = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            short=self.short,
            original=self.original,
            timestamp=self.timestamp,
        )
    fields = {
        'url': 'original',
        'custom_id': 'short',
        'timestamp': 'timestamp'
    }

    def from_dict(self, data):
        for field in ['url', 'custom_id', 'timestamp']:
            if field in data:
                setattr(self, self.fields[field], data[field])
