import datetime

class Scheduler:
    def __init__(self):
        self.tasks = []  # Each task: {subject, summary, deadline (optional), added_at}

    def add_task(self, subject, summary, deadline=None):
        self.tasks.append({
            "subject": subject,
            "summary": summary,
            "deadline": deadline,
            "added_at": datetime.datetime.now()
        })

    def get_upcoming_tasks(self, within_days=7):
        now = datetime.datetime.now()
        upcoming = []
        for task in self.tasks:
            if task["deadline"]:
                try:
                    deadline_dt = datetime.datetime.fromisoformat(task["deadline"])
                    if 0 <= (deadline_dt - now).days <= within_days:
                        upcoming.append(task)
                except Exception:
                    continue
        return upcoming

    def get_all_tasks(self):
        return self.tasks 