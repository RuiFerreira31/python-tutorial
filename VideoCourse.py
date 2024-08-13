from Course import Course


class VideoCourse(Course):

    def __init__(self, title, instructor, price, length_video):
        super().__init__(title, instructor, price)
        self.length_video = length_video

    def show_details(self):
        details = super().show_details()
        details += f"Length of Video: {self.length_video} hours\n"
        return details


video_course = VideoCourse("Python Programming", "John Doe", 99, 10.5)
video_course.new_user_enrolled("Alice")
video_course.received_a_rating(4.5)
video_course.received_a_rating(5.0)
print(video_course)
print("\nVideo Course Details:")
print(video_course.show_details())