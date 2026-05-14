from django.core.mail import EmailMultiAlternatives
from doctors.models import Specialization
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def send_email_thread(subject, body, to_email):
    email = EmailMultiAlternatives(
        subject,
        body="Your appointment has been confirmed successfully.",
        to=[to_email]
    )
    email.attach_alternative(body, "text/html")
    email.send()


def analyze_symptoms(symptoms):

    valid_specializations = list(
        Specialization.objects.values_list("name", flat=True)
    )

    specialization_list = ", ".join(valid_specializations)

    prompt = f"""
    You are a strict medical triage assistant.

    ========================
    INPUT VALIDATION
    ========================
    If symptoms are meaningless (hi, hehe, ok, test, random text, etc.):
    - Specialization: Invalid Input
    - Severity: unknown
    - Response: Ask user to enter real symptoms.

    ========================
    USER INPUT
    ========================
    Symptoms: {symptoms}

    IMPORTANT:
    - Extract duration from the text if mentioned.
    - If not mentioned, assume unknown.

    Allowed specializations:
    {specialization_list}

    ========================
    OUTPUT FORMAT (STRICT)
    ========================
    Specialization: <value>
    Severity: low/medium/high/unknown
    Response: <message>
    """
    model = genai.GenerativeModel('gemini-2.5-flash')
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

    except Exception as e:
        return {
            "is_valid": False,
            "specialization": "General Medicine",
            "severity": "unknown",
            "response": f"Error analyzing symptoms: {str(e)}",
        }

    specialization = "Invalid Input"
    severity = "unknown"
    ai_response = text

    try:
        for line in text.split("\n"):
            if line.startswith("Specialization:"):
                specialization = line.replace("Specialization:", "").strip()

            elif line.startswith("Severity:"):
                severity = line.replace("Severity:", "").strip().lower()

            elif line.startswith("Response:"):
                ai_response = line.replace("Response:", "").strip()

    except Exception:
        pass

    # validate specialization match
    if specialization != "Invalid Input":
        matched = next(
            (s for s in valid_specializations if s.lower() == specialization.lower()),
            None
        )
        
        if not matched:
            matched = next(
                (s for s in valid_specializations if specialization.lower() in s.lower() or s.lower() in specialization.lower()),
                "General Medicine"
            )
        specialization = matched

    is_valid = specialization.lower() != "invalid input"

    return {
        "is_valid": is_valid,
        "specialization": specialization,
        "severity": severity,
        "response": ai_response,
    }
