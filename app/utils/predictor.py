import joblib
import pandas as pd

class MalariaPredictor:
    FEATURE_MAP = {
            'geopolitical_zone_3': lambda x: int(x['geopolitical_zone'] == 3),
            'residence_type_2':    lambda x: int(x['residence_type'] == 2),
            'water_source_14':     lambda x: int(x['water_source'] == 14),
            'water_source_21':     lambda x: int(x['water_source'] == 21),
            'water_source_31':     lambda x: int(x['water_source'] == 31),
            'water_source_32':     lambda x: int(x['water_source'] == 32),
            'water_source_43':     lambda x: int(x['water_source'] == 43),
            'floor_material_34':   lambda x: int(x['floor_material'] == 34),
            'wall_material_22':    lambda x: int(x['wall_material'] == 22),
            'wall_material_31':    lambda x: int(x['wall_material'] == 31),
            'wall_material_34':    lambda x: int(x['wall_material'] == 34),
            'roof_material_31':    lambda x: int(x['roof_material'] == 31),
            'sex_2':               lambda x: int(x['sex'] == 2),
            'has_electricity_1':   lambda x: int(x['has_electricity'] == 1),
            'wealth_index':        lambda x: x['wealth_index'],
            'household_size':      lambda x: x['household_size'],
            'children_under5':     lambda x: x['children_under5'],
            'age':                 lambda x: x['age'],
            'net_type':            lambda x: x['net_type'],
            }
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.model_path = model_path 
    
    def _transform(self, user_inputs: dict):
        row = {feature: func(user_inputs) for feature, func in self.FEATURE_MAP.items()}
        return pd.DataFrame([row])

    def _categorize_risk(self, probability):
        if probability >= 0.65:
            risk_level = "High"
        elif probability >= 0.35:
                risk_level = "Medium"
        else:
             risk_level = "Low"
        return risk_level

    def predict(self, user_inputs: dict):
        transformed_inputs = self._transform(user_inputs)
        prediction = self.model.predict(transformed_inputs)
        probability = self.model.predict_proba(transformed_inputs)[:, 1]
        risk_level = self._categorize_risk(probability[0])
        return {
            "prediction": int(prediction[0]),
            "probability": float(probability[0]),
            "risk_level": risk_level
        }