import csv
import logging
import os
from fetcher.freelancer_api import FreelancerAPI


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

OUTPUT_CSV = "data/projects.csv"

def main():
   
    token = os.getenv("FREELANCER_OAUTH_TOKEN", "YOUR_FREELANCER_TOKEN") # Get your API token from freelancer.com

   
    freelancer_client = FreelancerAPI(oauth_token=token)

    
    projects_data = freelancer_client.fetch_ai_projects(limit=20) #limit used to project it from spam and not to get banned

    if not projects_data:
        logger.warning("No projects data retrieved. Exiting.")
        return

    logger.info(f"Writing {len(projects_data)} projects to CSV...")
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "project_id", 
                "title", 
                "description", 
                "budget_min", 
                "budget_max", 
                "posted_date", 
                "skills", 
                "client_country"
            ]
        )
        writer.writeheader()
        for row in projects_data:
            writer.writerow(row)

    logger.info(f"Data writing complete! See {OUTPUT_CSV}.")

if __name__ == "__main__":
    main()

