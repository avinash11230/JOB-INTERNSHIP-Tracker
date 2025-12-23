from api import fetch_jobs
from database import create_table, insert_jobs, get_jobs

def main():
    create_table()

    print("Fetching internship data...")
    jobs = fetch_jobs(role="intern", location="india", results=10)

    insert_jobs(jobs)
    print("Jobs saved to database.\n")

    print("Stored Opportunities:\n")
    all_jobs = get_jobs()

    for job in all_jobs:
        print(f"Company: {job[1]}")
        print(f"Role: {job[2]}")
        print(f"Location: {job[3]}")
        print(f"Status: {job[5]}")
        print("-" * 40)

if __name__ == "__main__":
    main()
