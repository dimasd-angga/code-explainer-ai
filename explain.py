import argparse
import os
import requests
import time

def explain_with_openai(code, api_key):
    """Use OpenAI API for explanation"""
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Explain code in simple terms for beginners."},
            {"role": "user", "content": f"Explain this code:\n\n{code}\n\nFocus on:" + 
             "\n1. Purpose\n2. Key components\n3. Example usage\n4. Common pitfalls"}
        ],
        "temperature": 0.3,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            print("⚠️ OpenAI API rate limit reached. Waiting 20 seconds...")
            time.sleep(20)
            return explain_with_openai(code, api_key)
        print(f"OpenAI Error: {e}")
    except Exception as e:
        print(f"API Error: {e}")
    return None

def explain_with_fallback(code):
    """Free fallback using local analysis"""
    print("ℹ️ Using basic explanation (no AI)...")
    return f"""Basic Code Analysis:
- This appears to be a {'function' if 'def ' in code else 'code snippet'}
- Key operations: {', '.join(find_keywords(code))}
- Try adding comments to understand it better!"""

def find_keywords(code):
    """Extract programming keywords"""
    keywords = set()
    for word in ['def', 'return', 'if', 'else', 'for', 'while', 'import']:
        if word in code:
            keywords.add(word)
    return keywords or {'unknown'}

def main():
    parser = argparse.ArgumentParser(description='AI-powered code explainer')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help='Code text to explain')
    group.add_argument('-f', '--file', help='File containing code to explain')
    
    args = parser.parse_args()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if args.file:
        try:
            with open(args.file, 'r') as f:
                code = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        code = args.text
    
    print("\n🧠 Generating explanation...\n")
    
    explanation = None
    if api_key:
        explanation = explain_with_openai(code, api_key)
    
    if not explanation:
        explanation = explain_with_fallback(code)
    
    print("💡 Code Explanation:")
    print("-" * 50)
    print(explanation)
    print("-" * 50)

if __name__ == "__main__":
    main()
