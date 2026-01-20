from google import genai
from google.genai import types


API_KEY = "AIzaSyBrmSnkypBDMPGDPNtUZgMwMPHyrSDKNOA" 

client = genai.Client(api_key=API_KEY)

system_instruction = """
You are 'Vajra-AI', a cybersecurity expert for Indian users.
Analyze the given text for fraud/phishing.
Output format:
1. Risk Score: (0-100%)
2. Verdict: (SAFE or SCAM)
3. Reason: (One line in English)
4. Hindi Explanation: (Explain to a rural user why this is dangerous in Hinglish/Hindi)
"""

# Test Message (Ye ek nakli scam message hai check karne ke liye)
user_message = "Dear Customer, Your SBI YONO account will be blocked today. Pan card not updated. Click link to update: http://bit.ly/fake-link"

print(f"Checking Message: {user_message}\n" + "-"*30)

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=system_instruction + f"\n\nMessage to analyze: {user_message}"
    )
    print(response.text)

except Exception as e:
    print(f"Error aaya: {e}")