from application import db

class World(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    total_cases = db.Column(db.Float, nullable=False)
    total_recovered = db.Column(db.Float, nullable=False)
    critical_active = db.Column(db.Float, nullable=False)
    total_deaths = db.Column(db.Float, nullable=False)
    non_critical_active = db.Column(db.Float, nullable=False)
    date_processed = db.Column(db.String(8), nullable=False)
    total_recovered_percentage = db.Column(db.Float, nullable=False)
    critical_active_percentage = db.Column(db.Float, nullable=False)
    total_deaths_percentage = db.Column(db.Float, nullable=False)
    non_critical_active_percentage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Post('{self.total_cases}', '{self.total_recovered}','{self.critical_active}','{self.total_deaths}','{self.non_critical_active}','{self.date_processed}','{self.total_recovered_percentage}','{self.critical_active_percentage}','{self.total_deaths_percentage}','{self.non_critical_active_percentage}')"


class Continents(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    total_cases = db.Column(db.Float, nullable=False)
    total_recovered = db.Column(db.Float, nullable=False)
    critical_active = db.Column(db.Float, nullable=False)
    total_deaths = db.Column(db.Float, nullable=False)
    non_critical_active = db.Column(db.Float, nullable=False)
    date_processed = db.Column(db.String(8), nullable=False)
    total_recovered_percentage = db.Column(db.Float, nullable=False)
    critical_active_percentage = db.Column(db.Float, nullable=False)
    total_deaths_percentage = db.Column(db.Float, nullable=False)
    non_critical_active_percentage = db.Column(db.Float, nullable=False)
    continent = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Post('{self.total_cases}', '{self.total_recovered}','{self.critical_active}','{self.total_deaths}','{self.non_critical_active}','{self.date_processed}','{self.total_recovered_percentage}','{self.critical_active_percentage}','{self.total_deaths_percentage}','{self.non_critical_active_percentage}','{self.continent}')"


class Countries(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    total_cases = db.Column(db.Float)
    total_recovered = db.Column(db.Float)
    critical_active = db.Column(db.Float)
    total_deaths = db.Column(db.Float)
    non_critical_active = db.Column(db.Float)
    date_processed = db.Column(db.String(8))
    total_recovered_percentage = db.Column(db.Float)
    critical_active_percentage = db.Column(db.Float)
    total_deaths_percentage = db.Column(db.Float)
    non_critical_active_percentage = db.Column(db.Float)
    continent = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __repr__(self):
        return f"Post('{self.total_cases}', '{self.total_recovered}','{self.critical_active}','{self.total_deaths}','{self.non_critical_active}','{self.date_processed}','{self.total_recovered_percentage}','{self.critical_active_percentage}','{self.total_deaths_percentage}','{self.non_critical_active_percentage}','{self.continent}','{self.country}')"
