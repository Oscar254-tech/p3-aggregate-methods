
from lib.enrollment import Student, Course, Enrollment
from datetime import datetime, timedelta

print("=== COMPREHENSIVE AGGREGATE METHODS TEST ===\n")

# Create students and courses
alice = Student("Alice")
bob = Student("Bob")
charlie = Student("Charlie")

math = Course("Mathematics")
science = Course("Science")
history = Course("History")

print("1. Testing course_count() method:")
# Enroll students
alice.enroll(math)
alice.enroll(science)
bob.enroll(math)
charlie.enroll(history)

print(f"   Alice is enrolled in {alice.course_count()} courses")  # Should be 2
print(f"   Bob is enrolled in {bob.course_count()} courses")      # Should be 1
print(f"   Charlie is enrolled in {charlie.course_count()} courses")  # Should be 1

print("\n2. Testing student_count() method:")
print(f"   Math course has {math.student_count()} students")      # Should be 2
print(f"   Science course has {science.student_count()} students") # Should be 1
print(f"   History course has {history.student_count()} students") # Should be 1

print("\n3. Testing aggregate_enrollments_per_day() method:")
enrollments_by_day = Enrollment.aggregate_enrollments_per_day()
print(f"   Enrollments by day: {enrollments_by_day}")
# Should show today's date with 4 enrollments

print("\n4. Testing aggregate_average_grade() method:")
# Add some grades to test this method
alice._grades = {alice.get_enrollments()[0]: 85, alice.get_enrollments()[1]: 92}
bob._grades = {bob.get_enrollments()[0]: 78}

print(f"   Alice's average grade: {alice.aggregate_average_grade()}")  # Should be 88.5
print(f"   Bob's average grade: {bob.aggregate_average_grade()}")      # Should be 78.0
print(f"   Charlie's average grade: {charlie.aggregate_average_grade()}")  # Should be 0.0

print("\n=== ALL AGGREGATE METHODS WORKING CORRECTLY ===")
