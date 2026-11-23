
import requests
from collections import Counter

# Ollama configuration
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
MODEL = "llama3.2:1b"

# Read application logs
log_file = "logs/app.log"

with open(log_file, "r") as file:
    logs = file.readlines()

# Analyze log levels
log_levels = Counter()
error_messages = []

for line in logs:
    if "INFO" in line:
        log_levels["INFO"] += 1

    elif "WARNING" in line:
        log_levels["WARNING"] += 1

    elif "ERROR" in line:
        log_levels["ERROR"] += 1
        error_messages.append(line.strip())

    elif "CRITICAL" in line:
        log_levels["CRITICAL"] += 1
        error_messages.append(line.strip())

# Display log summary
print("\n===== DEVOPS LOG ANALYZER =====")
print("Total log entries:", len(logs))

print("\n===== LOG SUMMARY =====")

for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
    print(f"{level}: {log_levels[level]}")

print("\n===== DETECTED ERRORS =====")

for error in error_messages:
    print(error)

# Send errors to local AI
if error_messages:
    print("\n===== AI ERROR ANALYSIS =====")
    print("Analyzing errors using Llama AI...")

    prompt = f"""
    You are a DevOps engineer.

    Analyze these application log errors:

    {chr(10).join(error_messages)}

    Explain:
    1. What went wrong?
    2. What are the possible causes?
    3. How can a DevOps engineer fix these issues?

    Give simple and practical answers.
    """

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        ai_result = response.json()["response"]

        print("\n===== AI RECOMMENDATIONS =====")
        print(ai_result)

    except requests.exceptions.RequestException as error:
        print("AI connection error:", error)

else:
    print("\nNo errors detected.")

print("\n===== ANALYSIS COMPLETED =====")
