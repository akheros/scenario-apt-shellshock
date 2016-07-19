from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(10)
    def index(self):
        self.client.get("/")

    @task(9)
    def projects(self):
        self.client.get("/projects.html")

    @task(7)
    def booking(self):
        self.client.get("/booking.html")

    @task(1)
    def mail(self):
        self.client.get("/mail.html")

    @task(3)
    def blog(self):
        self.client.get("/blog.html")

    @task(5)
    def article(self):
        self.client.get("/single.html")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000

