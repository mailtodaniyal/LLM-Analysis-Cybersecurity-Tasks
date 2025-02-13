import openai
import os
import ollama
import logging

logging.basicConfig(filename="output.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    logging.error("OpenAI API key is missing. Set OPENAI_API_KEY environment variable.")
    raise ValueError("OpenAI API key is missing. Set OPENAI_API_KEY environment variable.")

def check_environment():
    logging.info("Checking environment setup...")
    if os.name == "nt":
        logging.info("Running on Windows 10")
    else:
        logging.warning("Warning: This script is optimized for Windows 10")

def safe_api_call(prompt, model="gpt-4-turbo", temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": prompt}],
            temperature=temperature
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return "Error: API call failed. Check logs."

def generate_haiku():
    logging.info("Generating Knoxville-themed haiku...")
    prompt = "Write a Knoxville-themed haiku in a poetic style."
    haiku = safe_api_call(prompt)
    logging.info(f"Generated Haiku: {haiku}")
    return haiku

def analyze_model():
    logging.info("Analyzing LLM model training data and architecture...")
    prompt = "Describe the training data and architecture of GPT-4, including how it processes images."
    analysis = safe_api_call(prompt)
    logging.info(f"Model Analysis: {analysis}")
    return analysis

def geolocate_image():
    logging.info("Performing step-by-step image geolocation analysis...")
    prompt = "Analyze this image’s features (e.g., landmarks, weather, signs) to determine the location. Think step by step."
    geolocation_analysis = safe_api_call(prompt, temperature=0.6)
    logging.info(f"Geolocation Analysis: {geolocation_analysis}")
    return geolocation_analysis

def audit_code():
    logging.info("Performing code security audit...")
    sample_code = """
import os
password = input("Enter password: ")
if password == "admin123":
    os.system("rm -rf /")
"""
    prompt = f"Find and explain security vulnerabilities in the following Python code:\n{sample_code}"
    security_analysis = safe_api_call(prompt)
    logging.info(f"Code Security Audit: {security_analysis}")
    return security_analysis

def compare_logos():
    logging.info("Comparing AI-generated logos vs. real logos...")
    prompt = "Compare AI-generated logos with real logos like Chase.com’s. How can an LLM generate more realistic imitations?"
    logo_analysis = safe_api_call(prompt)
    logging.info(f"Logo Design Analysis: {logo_analysis}")
    return logo_analysis

if __name__ == "__main__":
    check_environment()
    generate_haiku()
    analyze_model()
    geolocate_image()
    audit_code()
    compare_logos()
    logging.info("Task Execution Completed. Logs stored in output.log.")
    print("\n[✔] Task Execution Completed. Logs stored in output.log.")
