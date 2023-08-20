from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd

# Load the dataset
df = pd.read_json(r"C:\Users\Jasmehr\Downloads\cleaned_flipkart_fashion_products_dataset.json")

# Implement your recommendation algorithm
def get_recommendations(product):
    # Replace this with your recommendation algorithm
    # For demonstration purposes, let's return the top 5 products with the same category as the input product
    category = df[df['product_name'] == product]['category'].iloc[0]
    recommendations = df[df['category'] == category]['product_name'].head(5).tolist()
    return recommendations

class ActionRecommendProduct(Action):
    def name(self):
        return "action_recommend_product"

    def run(self, dispatcher, tracker, domain):
        # Extract the product slot value
        product = tracker.get_slot('product')

        # Get recommendations
        recommendations = get_recommendations(product)

        # Send the recommendations to the user
        dispatcher.utter_message(text=f"Here are some recommendations for {product}: {', '.join(recommendations)}")

        return [SlotSet('product', product)]
