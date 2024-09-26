from repository.database import create_tables
import logging
from flask import Flask
from controlers.target_controler import target_bluprint,get_all_targets
from dictalchemy.utils import asdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    app.register_blueprint(target_bluprint, url_prefix="/api/mission")

    app.run(debug=True)
