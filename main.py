from gmail_agent import authenticate_gmail, get_and_summarize_emails
from scheduler import Scheduler
from recommender import Recommender
import re

def extract_deadline(summary):
    if not isinstance(summary, str):
        return None
    # Simple regex to find date in YYYY-MM-DD or YYYY-MM-DDTHH:MM format
    match = re.search(r'(\d{4}-\d{2}-\d{2}(T\d{2}:\d{2})?)', summary)
    return match.group(1) if match else None

def main():
    print("Authenticating with Gmail...")
    service = authenticate_gmail()
    print("Fetching and summarizing emails...")
    summaries = get_and_summarize_emails(service, num_emails=3)  # Limit to 3 emails

    scheduler = Scheduler()
    for item in summaries:
        deadline = extract_deadline(item['summary'])
        scheduler.add_task(item['subject'], item['summary'], deadline)

    print("\nUpcoming Tasks:")
    for task in scheduler.get_upcoming_tasks():
        print(f"- {task['subject']} (Deadline: {task['deadline']})\n  {task['summary']}")

    recommender = Recommender()
    print("\nProductivity Suggestions:")
    for suggestion in recommender.suggest_routines(scheduler.get_all_tasks()):
        print(f"- {suggestion}")

if __name__ == "__main__":
    main()
