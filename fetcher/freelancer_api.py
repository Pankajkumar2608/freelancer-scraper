# fetcher/freelancer_api.py

import logging
from freelancersdk.session import Session
from freelancersdk.resources.projects import search_projects
from .ratelimiter import rate_limited_request

logger = logging.getLogger(__name__)

class FreelancerAPI:
    def __init__(self, oauth_token: str):
        """
        Initialize with a valid Freelancer.com OAuth2 token [6].
        """
        self.session = Session(oauth_token=oauth_token)

    def fetch_ai_projects(self, limit=10):
        """
        Fetch AI-related projects from Freelancer.
        We use the official SDK's search_projects() resource [6].
        """
        logger.info("Fetching AI-related projects from Freelancer...")
        try:
            # The 'search_projects' method expects certain parameters [6]
            # Here we search for "AI" (q="AI") in active projects
            # 'limit' sets how many results to return per call
            response = rate_limited_request(
                search_projects, 
                self.session, 
                q="AI", 
                limit=limit 
            )

            if "projects" not in response:
                logger.warning("No 'projects' found in response.")
                return []

            data_list = []
            for proj in response["projects"]:
                # Safely extract relevant fields; if missing, use fallback
                project_id = proj.get("id")
                title = proj.get("title", "")
                description = proj.get("description", "")
                # "budget" is often an object with 'minimum' & 'maximum'
                budget_min = proj.get("budget", {}).get("minimum")
                budget_max = proj.get("budget", {}).get("maximum")
                # "time_submitted" is the posted timestamp
                posted_date = proj.get("time_submitted")
                # "jobs" is an array of skill objects
                skill_list = [job.get("name") for job in proj.get("jobs", [])]
                # "owner_id" leads us to the user info in "users" dict, if available
                owner_id = proj.get("owner_id")
                country = None
                if "users" in response and str(owner_id) in response["users"]:
                    user_info = response["users"][str(owner_id)]
                    country = user_info.get("location", {}).get("country", {}).get("name")

                data_list.append({
                    "project_id": project_id,
                    "title": title,
                    "description": description,
                    "budget_min": budget_min,
                    "budget_max": budget_max,
                    "posted_date": posted_date,
                    "skills": skill_list,
                    "client_country": country
                })

            logger.info(f"Fetched {len(data_list)} AI-related projects.")
            return data_list

        except Exception as e:
            logger.error(f"Error fetching AI projects: {e}")
            return []
