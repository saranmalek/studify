from django.http import HttpResponse
from django.shortcuts import render
# from .models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai

def homePage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"login.html")
def registerPage(request):
    return render(request,"registration.html")
def afterhomePage(request):
    return render(request,"afterhome.html")
def aboutPage(request):
    return render(request,"about.html")
def contactPage(request):
    return render(request,"Contact.html")
def eassyPage(request):
    return render(request,"eassy.html")
def homeworkPage(request):
    return render(request,"homework.html")
def GKPage(request):
    return render(request,"gkbot.html")
def punctuationPage(request):
    return render(request,"punctuation.html")
def quizPage(request):
    return render(request,"quiz.html")


# essay tool
# Configure API with your key
genai.configure(api_key="AIzaSyAmOnPDfEJQ3LtoTE2N9BekRg3iGswABOI")

@csrf_exempt
def generate_essay(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON request
            data = json.loads(request.body)
            topic = data.get("topic")   # Get the topic from the request body
            length = data.get("length") # Get the length (short, medium, long)
            essay_type = data.get("type")  # Get the essay type (argumentative, expository, etc.)

            # Construct the prompt based on provided values
            prompt = f"Write a {length} {essay_type} essay on '{topic}' in paragrapg only ."

            # Use the Generative Model to generate the essay based on the prompt
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Return the generated essay as a JSON response
            return JsonResponse({"essay": response.text})
        
        except Exception as e:
            # If there is an error, return a failure response with the error message
            return JsonResponse({"error": str(e)}, status=500)
        

# GKBOT tool
genai.configure(api_key="AIzaSyAmOnPDfEJQ3LtoTE2N9BekRg3iGswABOI")

@csrf_exempt
def get_gk_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_question = data.get("question")  # Get user question

            prompt = f"Answer the following general knowledge question: {user_question}"

            # You can replace "models/gemini-1.5-flash" with the appropriate model
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Return the response from the API
            return JsonResponse({"answer": response.text})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        


# Homework tool
genai.configure(api_key="AIzaSyAmOnPDfEJQ3LtoTE2N9BekRg3iGswABOI")

@csrf_exempt
def get_homework_solution(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON request data
            data = json.loads(request.body)
            user_question = data.get("question")  # Extract the question from the body
            
            if not user_question:
                return JsonResponse({"error": "No question provided."}, status=400)

            # Construct the prompt to pass to the AI model (example for general question answering)
            prompt = f"Answer the following question: {user_question} answers in this form question number(Q1) and then Ans:"

            # Generate content using the model (example with genai or replace with your model)
            model = genai.GenerativeModel("models/gemini-1.5-flash")  # You can use other models as required
            response = model.generate_content(prompt)

            # Return the generated solution in the JSON response
            return JsonResponse({"answer": response.text}, status=200)
        
        except Exception as e:
            # Handle exceptions and return error message
            return JsonResponse({"error": str(e)}, status=500)


# Configure the GenAI API key
genai.configure(api_key="AIzaSyAmOnPDfEJQ3LtoTE2N9BekRg3iGswABOI")

@csrf_exempt
def generate_quiz(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON request data
            data = json.loads(request.body)
            topic = data.get("topic")  # Extract the topic
            quiz_type = data.get("quiz_type")  # Extract the quiz type
            num_questions = int(data.get("num_questions", 10))  # Extract the number of questions (default to 10)

            if not topic:
                return JsonResponse({"error": "No topic provided."}, status=400)

            # Construct the prompt for quiz generation
            prompt = f"Create a {quiz_type} question quiz on the topic '{topic}' with {num_questions} in the form of Q1(no bold style) and so on with answers in last Ans:."

            # Use genai to generate the quiz content
            model = genai.GenerativeModel("models/gemini-1.5-flash")  # You can use any other model as required
            response = model.generate_content(prompt)

            # Return the generated quiz in the response
            return JsonResponse({"generated_quiz": response.text}, status=200)

        except Exception as e:
            # Handle exceptions and return an error message
            return JsonResponse({"error": str(e)}, status=500)
        
#punctuation
genai.configure(api_key="AIzaSyAmOnPDfEJQ3LtoTE2N9BekRg3iGswABOI")

@csrf_exempt
def correct_punctuation(request):
    if request.method == "POST":
        try:
            # Get the text from the POST request
            data = json.loads(request.body)
            user_text = data.get("text")  # Extract the user input text

            if not user_text:
                return JsonResponse({"error": "No text provided."}, status=400)

            # Construct the prompt for punctuation correction
            prompt = f"Correct the punctuation and grammar in the following text: {user_text}"

            # Use Gemini API to process the text
            model = genai.GenerativeModel("models/gemini-1.5-flash")  # Use the required model
            response = model.generate_content(prompt)

            # Return the corrected text
            corrected_text = response.text
            return JsonResponse({"corrected_text": corrected_text}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)