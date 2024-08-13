class Course:
    def __init__(self, title, instructor, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = 0
        self.users = []
        self.ratings = []
        self.avg_rating = 0.0

    def __str__(self):
        return (f"Course Title: {self.title}, Instructor: {self.instructor}, Price: ${self.price}, "
                f"Average Rating: {self.avg_rating:.1f}")

    def new_user_enrolled(self, new_user):
        self.users.append(new_user)

    def received_a_rating(self, new_rating):
        if new_rating>0:
            self.ratings.append(new_rating)
            self.avg_rating = sum(self.ratings) / len(self.ratings)

    def show_details(self):
        details = f"Title: {self.title}\nInstructor: {self.instructor}\nPrice: ${self.price}\nLectures: {self.lectures}\n"
        details += f"Number of Users Enrolled: {len(self.users)}\nAverage Rating: {self.avg_rating:.1f}\n"
        return details
