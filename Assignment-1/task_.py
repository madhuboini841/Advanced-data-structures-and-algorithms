class Patient:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.id = patient_id
        self.next = None


class PatientList:
    def __init__(self):
        self.head = None

    # Insert patient at beginning
    def insert_patient(self, name, age, patient_id):
        new_patient = Patient(name, age, patient_id)
        new_patient.next = self.head
        self.head = new_patient
        print("Patient inserted:", name)

    # Delete patient by ID
    def delete_patient(self, patient_id):
        temp = self.head
        prev = None

        # If head node itself holds the ID
        if temp is not None and temp.id == patient_id:
            self.head = temp.next
            print("Patient deleted with ID:", patient_id)
            return

        # Search for the ID
        while temp is not None and temp.id != patient_id:
            prev = temp
            temp = temp.next

        # If patient not found
        if temp is None:
            print("Patient not found with ID:", patient_id)
            return

        # Unlink the node
        prev.next = temp.next
        print("Patient deleted with ID:", patient_id)

    # Display all patients
    def display(self):
        temp = self.head
        if temp is None:
            print("No patients in the list.")
            return

        print("\n--- Patient List ---")
        while temp is not None:
            print(f"Name: {temp.name}, Age: {temp.age}, ID: {temp.id}")
            temp = temp.next


# -------------------------
# Example Usage
# -------------------------
plist = PatientList()

plist.insert_patient("Ravi", 30, 101)
plist.insert_patient("Sita", 25, 102)
plist.insert_patient("Kiran", 40, 103)

plist.display()

plist.delete_patient(102)

plist.display()
