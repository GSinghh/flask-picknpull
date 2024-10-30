import json
from app.extensions import db
from app import create_app
from app.models import Make
from app.models import Model

app = create_app()

def add_makes_to_db():
    makes_file_path = 'app/static/makes.json'
    with open(makes_file_path, 'r') as makes_file:
        makes_data = json.load(makes_file)
    for make, make_id in makes_data.items():
        try: 
            with app.app_context():
                make_obj = Make(make_name = make, make_code = make_id)
                db.session.add(make_obj)
                db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
        
        
def add_models_to_db():
    models_file_path = 'app/static/models.json'
    with open(models_file_path, 'r') as models_file:
        models_data = json.load(models_file)
    for model, model_id in models_data.items():
        try:
            with app.app_context():
                model_obj = Model(model_name = model, model_code = model_id)
                db.session.add(model_obj)
                db.session.commit()
        except Exception as e:
            print(f"Error: {e}")
        
add_models_to_db()
add_makes_to_db()