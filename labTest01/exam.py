class Exam:
    def __init__(self,name,rollno,score):
        self.name=name
        self.rollno=rollno
        self.score=score
        
    def cheack_pass(self):
        if self.score >= 40:
            print("Status: Pass")
        else:
            print("Status: Fail")

    
    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Score: {self.score}")
        self.cheack_pass()


# Example usage
exam1 = Exam("lallu", 2012, 85)
exam2 = Exam("lalith", 2500, 35)

exam1.display_result()


exam2.display_result()

