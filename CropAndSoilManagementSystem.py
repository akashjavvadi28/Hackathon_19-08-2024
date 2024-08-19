class CropAndSoilManagementSystem:
    def __init__(self):
        self.crops_data = {
            'Wheat': {
                'soil_type': 'loamy', 
                'pH': (6.0, 7.5), 
                'climate': 'temperate', 
                'NPK': (60, 40, 20),
                'water_needs': 'medium',
                'growth_period': '120 days',
                'yield': '3.2 tons/ha'
            },
            'Rice': {
                'soil_type': 'clay', 
                'pH': (5.0, 6.5), 
                'climate': 'tropical', 
                'NPK': (50, 30, 30),
                'water_needs': 'high',
                'growth_period': '150 days',
                'yield': '4.0 tons/ha'
            },
            'Maize': {
                'soil_type': 'sandy', 
                'pH': (5.5, 7.0), 
                'climate': 'warm', 
                'NPK': (70, 50, 40),
                'water_needs': 'low',
                'growth_period': '90 days',
                'yield': '2.8 tons/ha'
            }
        }
        self.diseases_data = {
            'Wheat': {
                'yellow': "Possible Yellow Rust. Use appropriate fungicide. Rotate crops to prevent recurrence.",
                'brown': "Possible Brown Spot. Use fungicide and improve drainage. Consider resistant varieties."
            },
            'Rice': {
                'brown': "Possible Brown Spot. Use fungicide and improve drainage. Consider resistant varieties."
            }
        }

    def recommend_crop(self, soil_type, pH, climate, npk_levels):
        recommendations = []
        for crop, details in self.crops_data.items():
            print(f"Checking crop: {crop}")
            print(f"Expected soil_type: {details['soil_type']}, Given soil_type: {soil_type}")
            print(f"Expected pH range: {details['pH']}, Given pH: {pH}")
            print(f"Expected climate: {details['climate']}, Given climate: {climate}")
            print(f"Expected NPK levels: {details['NPK']}, Given NPK levels: {npk_levels}")
            
            if (details['soil_type'] == soil_type and 
                details['pH'][0] <= pH <= details['pH'][1] and 
                details['climate'] == climate and
                all(npk_levels[i] >= details['NPK'][i] for i in range(3))):
                recommendations.append(crop)
        return recommendations if recommendations else ["No suitable crops found for the given conditions."]

    def analyze_soil(self, pH, moisture, npk_levels):
        analysis = []
        if pH < 5.5:
            analysis.append("Soil is too acidic. Consider liming.")
        elif pH > 7.5:
            analysis.append("Soil is too alkaline. Consider adding sulfur.")
        
        if moisture < 20:
            analysis.append("Soil moisture is low. Consider irrigation.")
        
        if npk_levels[0] < 50:
            analysis.append("Nitrogen level is low. Consider adding a nitrogen-rich fertilizer.")
        if npk_levels[1] < 30:
            analysis.append("Phosphorus level is low. Consider adding a phosphorus-rich fertilizer.")
        if npk_levels[2] < 20:
            analysis.append("Potassium level is low. Consider adding a potassium-rich fertilizer.")
        
        return analysis if analysis else ["Soil is in good condition."]

    def identify_disease(self, crop, symptoms):
        if crop in self.diseases_data:
            for symptom in symptoms:
                if symptom in self.diseases_data[crop]:
                    return self.diseases_data[crop][symptom]
        return "No disease identified. Consult a local agricultural expert."

    def seasonal_advice(self, season, crop):
        advice = ""
        if season == 'Spring':
            advice = "Ideal for planting warm-season crops like maize and vegetables."
        elif season == 'Summer':
            advice = "Ensure regular irrigation and monitor for pests. Mulching can help retain soil moisture."
        elif season == 'Autumn':
            advice = "Prepare for harvest and consider planting cover crops like clover or vetch."
        elif season == 'Winter':
            advice = "Focus on soil health by adding compost. Consider winter crops like wheat."
        
        if crop in self.crops_data:
            advice += f" Special care needed for {crop} during {season}. Its growth period is {self.crops_data[crop]['growth_period']}, and it has {self.crops_data[crop]['water_needs']} water needs."
        
        return advice

    def explain_recommendations(self, crop):
        if crop in self.crops_data:
            details = self.crops_data[crop]
            explanation = (
                f"{crop} is suitable for {details['soil_type']} soil with a pH range of {details['pH'][0]} to {details['pH'][1]}.\n"
                f"It thrives in {details['climate']} climates and requires NPK levels of {details['NPK']}.\n"
                f"Growth period is {details['growth_period']} with {details['water_needs']} water needs.\n"
                f"Average yield is {details['yield']}."
            )
            return explanation
        return "No detailed information available for this crop."

def main():
    system = CropAndSoilManagementSystem()
    
    soil_type = input("Enter the soil type (loamy, clay, sandy): ").lower()
    pH = float(input("Enter the soil pH level (e.g., 6.5): "))
    climate = input("Enter the climate (temperate, tropical, warm): ").lower()
    npk_levels = list(map(int, input("Enter the NPK levels (e.g., 60 40 20): ").split()))
    crop = input("Enter the crop type (Wheat, Rice, Maize): ").capitalize()
    symptoms = input("Enter observed symptoms (comma-separated, e.g., yellow, brown): ").lower().split(',')
    season = input("Enter the current season (Spring, Summer, Autumn, Winter): ").capitalize()
    moisture = float(input("Enter the soil moisture level (e.g., 25): "))
    
    crop_recommendations = system.recommend_crop(soil_type, pH, climate, npk_levels)
    soil_analysis = system.analyze_soil(pH, moisture, npk_levels)
    disease_info = system.identify_disease(crop, symptoms)
    seasonal_advice = system.seasonal_advice(season, crop)
    
    print("\n--- Recommendations ---")
    print("Crop Recommendations:", crop_recommendations)
    for recommendation in crop_recommendations:
        print(system.explain_recommendations(recommendation))
    print("\nSoil Analysis:", soil_analysis)
    print("Disease Identification:", disease_info)
    print("Seasonal Advice:", seasonal_advice)

if __name__ == "__main__":
    main()
