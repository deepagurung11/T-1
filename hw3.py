from queue import Queue
def main():
    patient_queue= queue()
    while True:
        print("\n=== Patient registration and Appointment Scheduling===")
        print("1.Register Patient")
        print("2.Remove Patient(Done with appointment)")
        print("3.Display patient queue")
        print("4.Exit")

        choice=input("Enter the number you want to select:")
        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_queue(patient_queue)
        elif choice == "4":
            ("logging out")
            break
        else:
            print("Invalid choice. Please enter the above mentioned number.")

def register_patient(queue):
            patient_name= input("Name of patient:")
            queue.put(patient_name)
            print(f"patient '{patient_name}'registered sucessfully")

def remove_patient(queue):
           if queue.empty():
               print("Patient does not exist.")
           else:
              removed_patient = queue.get()
              print(f"Patient' {removed_patient}'removed after comploetion of appointment.")
              
    