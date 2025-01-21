# diffbot-quickstart
"A beginner-friendly tutorial to get started with Diffbot's API for extracting and structuring web data."

# Diffbot Starter Tutorial

This repository provides a beginner-friendly guide to using Diffbot's powerful APIs for extracting and structuring web data. Follow this tutorial to set up a working example and learn the basics of interacting with the Diffbot API.

---

## Prerequisites

- Python 3.x installed on your system.
- A Diffbot API token. Sign up for one at [Diffbot](https://www.diffbot.com/).
- Basic familiarity with Python and the command line.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diffbot-starter-tutorial.git
cd diffbot-starter-tutorial
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Libraries

Install the required Python libraries:
```bash
pip install requests python-dotenv
```

### 4. Set Up the API Token

1. Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

2. Add your Diffbot API token to the `.env` file:
   ```env
   DIFFBOT_API_TOKEN=your_actual_api_token_here
   ```

3. Ensure the `.env` file is listed in `.gitignore` to keep it private:
   ```bash
   echo ".env" >> .gitignore
   ```

---

## Running the Example

### Article Extraction Script

The `examples/article_extraction.py` script demonstrates how to extract structured data from an article URL using Diffbot's Article API.

#### Example Usage:
```bash
python examples/article_extraction.py
```

#### Expected Output:
The script will print structured data extracted from the given URL, such as the title, author, publish date, and content.

---

## File Structure

```
diffbot-starter-tutorial/
├── README.md          # This file
├── .env               # Contains your Diffbot API token (not tracked by Git)
├── .gitignore         # Specifies files to exclude from version control
├── examples/
│   ├── article_extraction.py  # Example script for article extraction
├── requirements.txt   # List of Python dependencies
├── LICENSE            # License file
```

---

## Troubleshooting

### Common Errors

1. **Missing API Token**
   - Ensure the `.env` file exists and contains your API token in this format:
     ```env
     DIFFBOT_API_TOKEN=your_actual_api_token_here
     ```

2. **`ModuleNotFoundError: No module named 'requests'`**
   - Install the `requests` library:
     ```bash
     pip install requests
     ```

3. **File Not Found Errors**
   - Ensure you're running the script from the correct directory or provide the full path to the script.

---

## Learn More

Explore Diffbot's documentation to learn about more APIs and advanced use cases: [Diffbot Docs](https://docs.diffbot.com/).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

