from Course import Course
from VideoCourse import VideoCourse


class PdfCourse(Course):

    def __init__(self, title, instructor, price, pages):
        super().__init__(title, instructor, price)
        self.pages = pages

    def show_details(self):
        details = super().show_details()
        details += f"Number of Pages: {self.pages}\n"
        return details


pdf_course = PdfCourse("Python Programming Guide", "Jane Doe", 49, 250)
pdf_course.new_user_enrolled("Bob")
pdf_course.received_a_rating(4.0)
print(pdf_course)
print("\nPDF Course Details:")
print(pdf_course.show_details())