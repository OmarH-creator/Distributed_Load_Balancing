class Scheduler:
    def __init__(self, load_balancer):
        self.load_balancer = load_balancer

    def handle_request(self, request):
        worker = self.load_balancer.get_worker()
        return worker.process(request)