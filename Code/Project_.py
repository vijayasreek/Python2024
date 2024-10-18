#                Project Title
# " Athlete Health Tracking and Appointment Scheduler "  
class Athlete:
    def __init__(self, athlete_id, name, age, sport):
        """
        Initializes an Athlete object.
        :param athlete_id: Unique ID for the athlete.
        :param name: Name of the athlete.    
        :param age: Age of the athlete.
        :param sport: Sport played by the athlete.
        """
        self.athlete_id = athlete_id
        self.name = name
        self.age = age
        self.sport = sport
        self.health_progress = []  # List to track health progress

    def add_health_progress(self, progress_data):
        """
        Adds health progress data for the athlete.
        :param progress_data: A dictionary of health progress details.
        """
        self.health_progress.append(progress_data)

    def view_health_progress(self):
        """
        Returns the health progress of the athlete.
        """
        return self.health_progress


class Appointment:
    def __init__(self, appointment_id, athlete_id, date, time, reason):
        """
        Initializes an Appointment object.
        :param appointment_id: Unique ID for the appointment.
        :param athlete_id: ID of the athlete for whom the appointment is scheduled.
        :param date: Date of the appointment.
        :param time: Time of the appointment.
        :param reason: Reason for the appointment (e.g., injury check, physio).
        """
        self.appointment_id = appointment_id
        self.athlete_id = athlete_id
        self.date = date
        self.time = time
        self.reason = reason


class Clinic:
    def __init__(self):
        """
        Initializes a Clinic object.
        Maintains dictionaries to store athletes and appointments.
        """
        self.athletes = {}  # Store athletes with athlete_id as key
        self.appointments = {}  # Store appointments with appointment_id as key

    def create_appointment(self):
        """
        Creates a new appointment for an athlete based on user input.
        """
        appointment_id = int(input("Enter Appointment ID: "))
        athlete_id = int(input("Enter Athlete ID: "))
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        time = input("Enter Appointment Time (HH:MM): ")
        reason = input("Enter Appointment Reason (e.g., Injury Check, Physiotherapy): ")

        if athlete_id in self.athletes:
            new_appointment = Appointment(appointment_id, athlete_id, date, time, reason)
            self.appointments[appointment_id] = new_appointment
            print(f"Appointment {appointment_id} created for athlete {athlete_id}.")
        else:
            print(f"Athlete {athlete_id} does not exist. Please add the athlete first.")

    def read_appointment(self):
        """
        Retrieves and prints details of an appointment based on user input.
        """
        appointment_id = int(input("Enter Appointment ID: "))
        appointment = self.appointments.get(appointment_id)
        if appointment:
            print(f"Appointment Details: {appointment.date}, {appointment.time}, {appointment.reason}")
        else:
            print(f"Appointment {appointment_id} not found.")

    def update_appointment(self):
        """
        Updates an existing appointment based on user input.
        """
        appointment_id = int(input("Enter Appointment ID: "))
        appointment = self.appointments.get(appointment_id)
        if appointment:
            date = input("Enter new date (leave blank to keep the current date): ")
            time = input("Enter new time (leave blank to keep the current time): ")
            reason = input("Enter new reason (leave blank to keep the current reason): ")

            if date:
                appointment.date = date
            if time:
                appointment.time = time
            if reason:
                appointment.reason = reason

            print(f"Appointment {appointment_id} updated.")
        else:
            print(f"Appointment {appointment_id} not found.")

    def delete_appointment(self):
        """
        Deletes an appointment based on user input.
        """
        appointment_id = int(input("Enter Appointment ID: "))
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print(f"Appointment {appointment_id} deleted.")
        else:
            print(f"Appointment {appointment_id} not found.")

    def manage_medical_appointments(self):
        """
        Lists all appointments for a specific athlete based on user input.
        """
        athlete_id = int(input("Enter Athlete ID: "))
        athlete_appointments = [appt for appt in self.appointments.values() if appt.athlete_id == athlete_id]
        if athlete_appointments:
            for a in athlete_appointments:
                print(f"Appointment on {a.date} at {a.time} for {a.reason}")
        else:
            print(f"No appointments found for athlete {athlete_id}.")

    def track_health_progress(self):
        """
        Tracks and updates the health progress of an athlete based on user input.
        """
        athlete_id = int(input("Enter Athlete ID: "))
        progress_data = input("Enter health progress details (e.g., Improving flexibility): ")
        athlete = self.athletes.get(athlete_id)
        if athlete:
            athlete.add_health_progress({"date": "2024-09-25", "progress": progress_data})
            print(f"Health progress for athlete {athlete_id} updated.")
        else:
            print(f"Athlete {athlete_id} not found.")

    def add_athlete(self):
        """
        Adds a new athlete to the system based on user input.
        """
        athlete_id = int(input("Enter Athlete ID: "))
        name = input("Enter Athlete Name: ")
        age = int(input("Enter Athlete Age: "))
        sport = input("Enter Athlete Sport: ")

        if athlete_id not in self.athletes:
            self.athletes[athlete_id] = Athlete(athlete_id, name, age, sport)
            print(f"Athlete {athlete_id} added.")
        else:
            print(f"Athlete {athlete_id} already exists.")

    def get_athlete(self):
        """
        Retrieves details of an athlete based on user input.
        """
        athlete_id = int(input("Enter Athlete ID: "))
        athlete = self.athletes.get(athlete_id)
        if athlete:
            print(f"Athlete {athlete_id}: {athlete.name}, Age: {athlete.age}, Sport: {athlete.sport}")
        else:
            print(f"Athlete {athlete_id} not found.")


# Initialize the Clinic
clinic = Clinic()

# Example of user interaction:
while True:
    print("\n1. Add Athlete")
    print("2. Create Appointment")
    print("3. View Appointment")
    print("4. Update Appointment")
    print("5. Delete Appointment")
    print("6. List Athlete's Appointments")
    print("7. Track Athlete Health Progress")
    print("8. Get Athlete Info")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        clinic.add_athlete()
    elif choice == '2':
        clinic.create_appointment()
    elif choice == '3':
        clinic.read_appointment()
    elif choice == '4':
        clinic.update_appointment()
    elif choice == '5':
        clinic.delete_appointment()
    elif choice == '6':
        clinic.manage_medical_appointments()
    elif choice == '7':
        clinic.track_health_progress()
    elif choice == '8':
        clinic.get_athlete()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")