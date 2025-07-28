class Recommender:
    def __init__(self):
        pass

    def suggest_routines(self, tasks):
        if not tasks:
            return ["No tasks found. Try to add some tasks to your schedule!"]
        suggestions = []
        morning_tasks = [t for t in tasks if t.get('deadline') and self._is_morning(t['deadline'])]
        afternoon_tasks = [t for t in tasks if t.get('deadline') and self._is_afternoon(t['deadline'])]
        evening_tasks = [t for t in tasks if t.get('deadline') and self._is_evening(t['deadline'])]
        if morning_tasks:
            suggestions.append(f"You have {len(morning_tasks)} tasks due in the morning. Consider a morning review routine.")
        if afternoon_tasks:
            suggestions.append(f"You have {len(afternoon_tasks)} tasks due in the afternoon. Try a post-lunch productivity sprint.")
        if evening_tasks:
            suggestions.append(f"You have {len(evening_tasks)} tasks due in the evening. Plan a wrap-up session before dinner.")
        if not suggestions:
            suggestions.append("Keep your schedule balanced. Review your tasks daily for best productivity.")
        return suggestions

    def _is_morning(self, iso_dt):
        try:
            hour = int(iso_dt[11:13])
            return 5 <= hour < 12
        except:
            return False

    def _is_afternoon(self, iso_dt):
        try:
            hour = int(iso_dt[11:13])
            return 12 <= hour < 17
        except:
            return False

    def _is_evening(self, iso_dt):
        try:
            hour = int(iso_dt[11:13])
            return 17 <= hour < 22
        except:
            return False 