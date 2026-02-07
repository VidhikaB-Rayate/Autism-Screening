import joblib
import numpy as np
import os

# Define feature columns for reference
COLUMNS = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10', 'Age','Sex','Jaundice','Family_ASD']

class ModelService:
    def __init__(self):
        self.model = None
        self.load_model()

    def get_resource_path(self, filename):
        # Go up one level from backend/ to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, filename)

    def load_model(self):
        try:
            model_path = self.get_resource_path("random_forest_model.pkl")
            if os.path.exists(model_path):
                self.model = joblib.load(model_path)
                print(f"Model loaded successfully from {model_path}")
            else:
                print(f"Error: Model not found at {model_path}")
        except Exception as e:
            print(f"Failed to load model: {e}")

    def predict(self, input_data: list):
        """
        Expects a list of 14 numerical values corresponding to COLUMNS.
        The first 10 values are the answers which need to be processed based on direction.
        """
        if self.model is None:
            raise ValueError("Model is not loaded.")
        
        if len(input_data) != 14:
            raise ValueError(f"Expected 14 features, got {len(input_data)}")

        # Direction array for the first 10 questions
        direction = np.array([1, -1, -1, -1, 0, -1, 1, -1, 0, 1])

        # Separate answers and other features
        answers = np.array(input_data[:10])
        other_features = input_data[10:]

        # Apply scoring logic
        processed_answers = []
        for a, d in zip(answers, direction):
            if d == -1:
                processed_answers.append(1 - a)
            else:
                processed_answers.append(a)
        
        # Combine processed answers with other features
        final_features = processed_answers + other_features

        # Impressions Logic
        IMPRESSION = [
            "Sensory sensitivity to everyday sounds",
            "Limited spontaneous pretend play",
            "Limited use of pointing to share interest",
            "Reduced interest in social interaction games",
            "Unusual seeking of physical closeness",
            "Inconsistent response to name",
            "Tendency to disengage / stare into space",
            "Reduced interaction with peers",
            "Excessive climbing / activity seeking",
            "Repetitive or unusual hand / finger movements"
        ]
        
        flagged_impressions = [
            imp for imp, v in zip(IMPRESSION, processed_answers) if v == 1
        ]

        arr = np.array(final_features).reshape(1, -1)
        prediction = self.model.predict(arr)[0]
        
        return {
            "prediction": int(prediction),
            "impressions": flagged_impressions
        }

# Global instance
model_service = ModelService()
