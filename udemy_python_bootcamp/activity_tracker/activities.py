

class Activities():
    
    list_of_activities = ["Hiking"]

    def add_actvities(self, user_input):
        self.list_of_activities.append(user_input.capitalize())
    
    def register_activity(self, activity, duration, distance=0) -> dict:
        register_activity = {"activity": activity, "duration": duration, "distance": distance}
        return register_activity



activities = Activities()
activities.add_actvities("indoor climbing")
print(activities.list_of_activities)

chosen_activity = activities.list_of_activities[0]
print(chosen_activity)

most_recent_activity = activities.register_activity(chosen_activity, 30, 2)
print(most_recent_activity)