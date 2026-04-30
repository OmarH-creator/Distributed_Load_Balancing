from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from common.models import Request
from common.config import MODE

def run_load_test(scheduler, num_users, max_threads):
    results = []

    def send_request(i):
        if MODE == "normal":
            query = "."
        else:
            query = "What is load balancing?"

        request = Request(id=i, query=query)
        return scheduler.handle_request(request)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(send_request, i) for i in range(num_users)]

        for future in tqdm(as_completed(futures), total=num_users, desc="Processing requests"):
            results.append(future.result())

    return results