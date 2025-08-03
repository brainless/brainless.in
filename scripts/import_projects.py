"""
This script imports project information from GitHub and saves it to a JSON file.

It fetches repositories from a configurable list of owners, filters for projects
with recent activity, and extracts relevant details like name, description,
languages, and a summary from the README.

The script requires a GitHub Personal Access Token with 'repo' scope.
Set the GITHUB_TOKEN environment variable in a .env file in the same directory.

To run the script:
  pip install -r requirements.txt
  python import_projects.py
"""

import os
import json
from github import Github, GithubException
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

# --- Configuration ---
OWNERS = ["brainless", "pixlie"]
OUTPUT_FILE = "website/src/data/projects.json"
MONTHS_OF_ACTIVITY = 12
MIN_COMMITS = 10
# ---------------------

def get_github_token(owner_name):
    """Retrieves the GitHub token for a specific owner from environment variables."""
    load_dotenv()
    token_name = f"GITHUB_TOKEN_{owner_name.upper()}"
    token = os.getenv(token_name)
    if not token:
        raise ValueError(f"{token_name} environment variable not set.")
    return token

def get_recently_active_repos(g, owner_name, min_commits):
    """Fetches repositories for an owner and filters for recent activity."""
    try:
        try:
            owner = g.get_user(owner_name)
        except GithubException:
            owner = g.get_organization(owner_name)

        repos = owner.get_repos()
        active_repos = []
        twelve_months_ago = datetime.now(timezone.utc) - timedelta(days=365)

        for repo in repos:
            if repo.pushed_at > twelve_months_ago:
                commits = repo.get_commits(since=twelve_months_ago)
                if commits.totalCount >= min_commits:
                    active_repos.append(repo)
        return active_repos
    except GithubException as e:
        if e.status == 403:
            print(f"Warning: Could not access repos for {owner_name}. Skipping.")
            return []
        else:
            raise e

def get_readme_summary(repo):
    """Extracts the first paragraph from the README as a summary."""
    try:
        readme = repo.get_readme()
        content = readme.decoded_content.decode("utf-8")
        # Find the first non-empty line
        for line in content.splitlines():
            if line.strip():
                return line.strip()
    except Exception:
        return ""
    return ""

def main():
    """Main function to fetch and process project data."""
    try:
        all_projects = []

        for owner in OWNERS:
            print(f"Fetching projects for {owner}...")
            try:
                token = get_github_token(owner)
                g = Github(token)
                active_repos = get_recently_active_repos(g, owner, MIN_COMMITS)

                for repo in active_repos:
                    print(f"  - Processing {repo.full_name}")
                    summary = get_readme_summary(repo)
                    project_data = {
                        "name": repo.name,
                        "description": repo.description,
                        "url": repo.html_url,
                        "stars": repo.stargazers_count,
                        "languages": repo.get_languages(),
                        "summary": summary,
                        "last_updated": repo.pushed_at.isoformat(),
                    }
                    all_projects.append(project_data)
            except ValueError as e:
                print(f"Warning: {e}. Skipping {owner}.")

        # Ensure the output directory exists
        output_dir = os.path.dirname(OUTPUT_FILE)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(OUTPUT_FILE, "w") as f:
            json.dump(all_projects, f, indent=2)

        print(f"\nSuccessfully saved {len(all_projects)} projects to {OUTPUT_FILE}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()