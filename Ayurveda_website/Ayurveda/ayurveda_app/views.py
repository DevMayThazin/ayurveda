from django.shortcuts import render

# Create your views here.

# your_app_name/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Used for demonstration purposes
import joblib

# Define the path to the model file (adjust the path as needed)
MODEL_FILE_PATH = 'modelForPrediction.pkl'

# Load the ML model
model = joblib.load(MODEL_FILE_PATH)

# This decorator is used for demonstration purposes to disable CSRF protection.
# In a real application, you should handle CSRF properly.
@csrf_exempt
def predict_disease(request):
    if request.method == 'POST':
        try:
            # Assuming you receive symptom data as a JSON object in the request
            symptom_data = request.POST.get('symptoms')

            # Perform any necessary preprocessing on symptom_data
            # ...

            # Make predictions using the loaded model
            predictions = model.predict(symptom_data)

            # Prepare the response JSON
            response_data = {
                'predictions': predictions.tolist(),
            }

            return JsonResponse(response_data)

        except Exception as e:
            # Handle any errors that occur during prediction
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=500)

    else:
        # Handle other HTTP methods (GET, PUT, DELETE) if needed
        return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)




def index_view(request):
    return render(request, 'ayurveda_app/index.html')

def faq_view(request):
    return render(request, 'ayurveda_app/faq.html')
def aboutus(request):
    return render(request, 'ayurveda_app/aboutus.html')
def contactus(request):
    return render(request, 'ayurveda_app/contactus.html')
def practitioner(request):
    return render(request, 'ayurveda_app/practitioner.html')
def patient(request):
    return render(request, 'ayurveda_app/Patient.html')
def prakriti(request):
    return render(request, 'ayurveda_app/prakriti.html')
