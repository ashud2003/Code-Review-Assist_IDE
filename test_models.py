import google.generativeai as genai

API_KEY = "AIzaSyD7Sky6N4h9AP3TMdRMXAOwwb_dsg028mM"
genai.configure(api_key=API_KEY)

print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
