import datetime

class ProjectTracker:
    def __init__(self, project_name):
        self.project_name = project_name
        self.departments = []
        self.changes_log = []
        self.weekly_meetings = []

    def add_department(self, department_name):
        self.departments.append({
            'name': department_name,
            'notified': False,
            'updates': []
        })
        print(f"Department '{department_name}' added.")

    def log_change(self, change_description):
        timestamp = datetime.datetime.now()
        self.changes_log.append({
            'timestamp': timestamp,
            'description': change_description
        })
        print(f"Change logged: '{change_description}' at {timestamp}")

        # Notify all departments
        for dept in self.departments:
            dept['notified'] = True
            dept['updates'].append({
                'timestamp': timestamp,
                'change': change_description
            })
            print(f"Department '{dept['name']}' notified.")

    def schedule_weekly_meeting(self, date, time):
        meeting_time = datetime.datetime.combine(date, time)
        self.weekly_meetings.append(meeting_time)
        print(f"Weekly meeting scheduled for {meeting_time}")

    def get_project_status(self):
        print(f"Project: {self.project_name}")
        print("Changes Log:")
        for change in self.changes_log:
            print(f" - {change['timestamp']}: {change['description']}")
        print("\nDepartments Notified:")
        for dept in self.departments:
            print(f" - {dept['name']}: Notified = {dept['notified']}")
        print("\nScheduled Weekly Meetings:")
        for meeting in self.weekly_meetings:
            print(f" - {meeting}")

    def get_department_updates(self, department_name):
        for dept in self.departments:
            if dept['name'] == department_name:
                print(f"Updates for {department_name}:")
                for update in dept['updates']:
                    print(f" - {update['timestamp']}: {update['change']}")
                return
        print(f"No updates found for department '{department_name}'.")

# Example usage:
tracker = ProjectTracker("Crafter Project")

# Adding departments
tracker.add_department("Development")
tracker.add_department("Marketing")
tracker.add_department("Finance")

# Logging a change
tracker.log_change("Updated project scope to include new features.")

# Scheduling weekly meetings
tracker.schedule_weekly_meeting(datetime.date(2024, 9, 5), datetime.time(18, 30))

# Get the current project status
tracker.get_project_status()

# Get updates for a specific department
tracker.get_department_updates("Development")