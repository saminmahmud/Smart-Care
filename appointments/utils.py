from django.core.mail import EmailMultiAlternatives
from doctors.models import Specialization
from google import genai
from django.conf import settings


def send_email_thread(subject, body, to_email):
    email = EmailMultiAlternatives(
        subject,
        body="Your appointment has been confirmed successfully.",
        to=[to_email]
    )
    email.attach_alternative(body, "text/html")
    email.send()


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def analyze_symptoms(symptoms, duration):

    valid_specializations = list(
        Specialization.objects.values_list(
            "name",
            flat=True
        )
    )

    specialization_list = ", ".join(valid_specializations)

    prompt = f"""
    You are a healthcare assistant AI.

    Analyze the patient's symptoms carefully.

    Symptoms:
    {symptoms}

    Duration:
    {duration}

    IMPORTANT RULES:

    1. You MUST choose ONLY ONE specialization
    from this list:

    {specialization_list}

    2. Return specialization EXACTLY as written in the list.

    3. Do NOT create new specialization names.

    4. Do NOT change spelling.

    5. Keep response short and helpful.

    Give response in this exact format:

    Specialization: specialization_name
    Severity: low/medium/high
    Response: short helpful response

    Only provide the format above.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    specialization = valid_specializations[0]
    severity = "low"
    ai_response = text

    try:

        lines = text.split("\n")

        for line in lines:

            if line.startswith("Specialization:"):

                specialization = line.replace(
                    "Specialization:",
                    ""
                ).strip()

            elif line.startswith("Severity:"):

                severity = line.replace(
                    "Severity:",
                    ""
                ).strip().lower()

            elif line.startswith("Response:"):

                ai_response = line.replace(
                    "Response:",
                    ""
                ).strip()

        matched_specialization = next(
            (
                spec for spec in valid_specializations
                if spec.lower() == specialization.lower()
            ),
            valid_specializations[0]
        )

        specialization = matched_specialization

    except Exception:
        pass

    return {
        "specialization": specialization,
        "severity": severity,
        "response": ai_response,
    }