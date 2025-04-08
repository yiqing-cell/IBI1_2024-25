class Patient(object):
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
        print(f"{self.name}, Age: {self.age}, Admission: {self.admission_date}, History: {self.medical_history}")

patient1 = Patient("Alice Smith", 34, "2025-04-01", "No allergies; Appendectomy in 2018")
