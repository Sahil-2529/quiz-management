#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Define the User class as the base class for Student, Teacher, and Parent
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} ({self.email})"


# Define the Student class, inheriting from User
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id


# Define the Teacher class, inheriting from User
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject


# Define the Parent class, inheriting from User
class Parent(User):
    def __init__(self, name, email, student):
        super().__init__(name, email)
        self.student = student


# Define the Quiz class
class Quiz:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.participants = []   # List to store participants
        self.submissions = {}    # Dictionary to store quiz submissions

    def add_participant(self, participant):
        self.participants.append(participant)
        self.submissions[participant.email] = None

    def enable_submissions(self):
        # Logic to enable quiz submissions (placeholder)
        pass

    def submit_quiz(self, participant, answers):
        if participant.email in self.submissions:
            self.submissions[participant.email] = answers
            print(f"{participant.name} submitted the quiz.")

    def get_quiz_results(self):
        results = {}
        for participant_email, answers in self.submissions.items():
            participant = next((p for p in self.participants if p.email == participant_email), None)
            if participant:
                score = self.calculate_score(answers)
                results[participant_email] = score
        return results

    def calculate_score(self, answers):
        # In this example, each correct answer gets 1 point
        correct_answers = {"Q1": "Option A", "Q2": "Option B", "Q3": "Option C"}
        score = 0
        for question, answer in answers.items():
            if answer == correct_answers.get(question):
                score += 1
        return score


# Define the QuizManagementSystem class
class QuizManagementSystem:
    def __init__(self):
        self.quizzes = []   # List to store created quizzes

    def create_quiz(self, name, teacher):
        quiz = Quiz(name, teacher)
        self.quizzes.append(quiz)
        return quiz

    def invite_participants(self, quiz, participants):
        for participant in participants:
            quiz.add_participant(participant)

    def display_results(self, quiz):
        results = quiz.get_quiz_results()
        if results:
            print(f"Quiz: {quiz.name} Results")
            for participant_email, score in results.items():
                participant = next((p for p in quiz.participants if p.email == participant_email), None)
                if participant:
                    print(f"{participant.name} ({participant.email}): {score}")
                else:
                    print(f"Unknown participant ({participant_email}): {score}")


# Sample code to demonstrate the usage of the Quiz Management System
if __name__ == "__main__":
    # Instantiate instances of the Student, Teacher, and Parent classes
    student1 = Student("Jim", "jim@example.com", "S12345")
    student2 = Student("Jack", "jack@example.com", "S67890")
    teacher = Teacher("Mr. Johnson", "johnson@example.com", "Mathematics")
    parent = Parent("Mrs. Joy", "mrs.joy@example.com", student1)

    # Create a quiz, invite participants, and add participants
    quiz_system = QuizManagementSystem()
    math_quiz = quiz_system.create_quiz("Math Quiz", teacher)
    quiz_system.invite_participants(math_quiz, [student1, student2, parent])

    # Enable quiz submissions and retrieve quiz results
    math_quiz.enable_submissions()

    # Simulate quiz submissions
    student1_answers = {"Q1": "Option A", "Q2": "Option B", "Q3": "Option C"}
    student2_answers = {"Q1": "Option B", "Q2": "Option A", "Q3": "Option C"}
    parent_answers = {"Q1": "Option A", "Q2": "Option B", "Q3": "Option D"}

    math_quiz.submit_quiz(student1, student1_answers)
    math_quiz.submit_quiz(student2, student2_answers)
    math_quiz.submit_quiz(parent, parent_answers)

    # Display quiz results
    quiz_system.display_results(math_quiz)


# In[ ]:




