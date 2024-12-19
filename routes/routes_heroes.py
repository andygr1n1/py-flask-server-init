from flask import jsonify
from sqlalchemy import text


class HeroRoutes:
    def __init__(self, app, session):
        self.app = app
        self.session = session
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/heroes', methods=['GET'])
        def heroes():
            try:
                result = self.session.execute(text("SELECT * FROM heroes")).fetchall()
                objects = [dict(row._mapping) for row in result]
                return jsonify({'message': 'success', 'heroes': objects}), 200
            except Exception as e:
                return jsonify({'message': 'error', 'error': str(e)}), 500
