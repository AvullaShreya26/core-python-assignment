# hospital_management.py

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Disease": self.disease}

def create_patient_list():
    p1 = Patient("Alice", 30, "Flu")
    p2 = Patient("Bob", 45, "Diabetes")
    p3 = Patient("Charlie", 35, "Flu")
    return [p1.to_dict(), p2.to_dict(), p3.to_dict()]

def search_by_disease(patients, disease):
    result = []
    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            result.append(patient["Name"])
    return result

if __name__ == "__main__":
    patients = create_patient_list()
    search_disease = "Flu"
    matching_patients = search_by_disease(patients, search_disease)
    print(f"Patients with {search_disease}: {matching_patients}")
