# AI Freelance Projects Collector

A simple Python application that retrieves *AI-related* project listings from Freelancer.com (using their Python SDK) and stores the results in a CSV file.

## Features
1. **Freelancer.com** API usage for searching “AI” projects
2. **Rate limiting** to avoid API overuse
3. **Logging** and **error handling**
4. Output to **CSV**

## Prerequisites
- Python 3.8+
- Valid Freelancer.com OAuth2 token (see below)
- Git (optional)

## Setup & Usage
1. Clone this repository:
    ```
    git clone https://github.com/Pankajkumar2608/freelancer-scraper.git
   
    ```
2. Create and activate a virtual environment (optional but recommended):
    ```
    python3 -m venv venv
    source venv/bin/activate  
    # or
    venv\Scripts\activate.bat 
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set your Freelancer OAuth token in the environment (or replace in code):
    ```
    export FREELANCER_OAUTH_TOKEN="YOUR_REAL_TOKEN"
    ```
5. Run the script:
    ```
    python main.py
    ```

## Data Output
- A CSV file named `projects.csv` will appear in the `data/` directory containing:
  - `project_id`
  - `title`
  - `description`
  - `budget_min`
  - `budget_max`
  - `posted_date`
  - `skills`
  - `client_country`

## Error Handling & Logging
- Logs are printed to stdout. Adjust log settings in `main.py` if needed.
- The script handles network/API errors and logs them at the `ERROR` level.

## Credentials Management
- For local development, you can set the environment variable `FREELANCER_OAUTH_TOKEN`.
- In production, use a secure secrets manager (e.g., AWS Secrets Manager, Vault).

## Sample CSV Snippet

