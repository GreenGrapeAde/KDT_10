class Student:
    def __init__(self, name, gender, grade):
        self.name = name
        self.gender = gender
        self.grade = grade
    
    def student_info(self):
        print(f"학생 이름: {self.name}, 성별: {self.gender}, 성적: {self.grade}")
    
    def change_grade(self, new_grade):
        old_grade = self.grade
        self.grade = new_grade
        print(f"{self.name}님의 기존 성적 {old_grade}가 {self.grade}로 변경되었습니다.")


student1 = Student("조주영", "남", 3.5)
student1.student_info()
student1.change_grade(4.0)