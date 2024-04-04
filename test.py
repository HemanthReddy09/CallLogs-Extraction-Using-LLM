import requests
import time

# Replace with your Flask app's URL
base_url = "http://127.0.0.1:5000/"

# Submit documents for processing
submit_url = f"{base_url}/submit_documents"
payload = {
    "question": "What are our product design decisions?",
    "documents": ["https://raw.githubusercontent.com/eliem08/rag-files/main/call_log_20240318_094500.txt", "https://raw.githubusercontent.com/eliem08/rag-files/main/call_log_20240317_101500.txt"],
    "autoApprove": True
}
response = requests.post(submit_url, json=payload)
print("Submission Response:", response.json())

# Poll for results
polling_url = f"{base_url}/get_question_and_facts"
while True:
    poll_response = requests.get(polling_url).json()
    print("Polling Response:", poll_response)
    if poll_response["status"] == "done":
        break
    time.sleep(2)  # Wait for a couple of seconds before polling again
