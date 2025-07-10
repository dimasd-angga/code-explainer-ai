# Code Explainer AI 🤖

A command-line tool that uses AI to explain complex code snippets in simple English. Perfect for learning and daily coding!

---

## Features
- Instant explanations for any code snippet
- Supports both direct input and file input
- Clear, beginner-friendly explanations
- Protects privacy (no code sent to external servers beyond OpenAI)

---

## Setup

### 1. Get OpenAI API Key
1. Create an account at [OpenAI](https://platform.openai.com/)
2. Get your API key from [API Keys dashboard](https://platform.openai.com/api-keys)

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install requests
```

### 4. Set Environment Variable

```bash
# Linux/macOS
export OPENAI_API_KEY='your_api_key_here'

# Windows (Command Prompt)
set OPENAI_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:OPENAI_API_KEY='your_api_key_here'
```

---

## Usage

```bash
# Explain code from text
python explain.py -t "def factorial(n): return 1 if n == 0 else n * factorial(n-1)"

# Explain code from file
python explain.py -f complex_algorithm.py
```

### Example

```bash
python explain.py -t "list(map(lambda x: x**2, [1,2,3]))"
```

### Output

```
🧠 Generating explanation...

💡 Code Explanation:
--------------------------------------------------
This code creates a list of squared numbers. Here's how it works:

1. `[1,2,3]` is our input list of numbers
2. `lambda x: x**2` creates a small function that squares its input
3. `map()` applies this squaring function to each element in the list
4. `list()` converts the result into a standard Python list

The final output will be [1, 4, 9]
--------------------------------------------------
```

---

## Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/improve-explanations
   ```
3. Commit changes  
   ```bash
   git commit -m 'Add better error handling'
   ```
4. Push to the branch  
   ```bash
   git push origin feature/improve-explanations
   ```
5. Open a pull request
