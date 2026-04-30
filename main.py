import time
from common.config import MODE, NUM_USERS, NUM_WORKERS, MAX_THREADS
from workers.gpu_worker import GPUWorker
from lb.load_balancer import LoadBalancer
from master.scheduler import Scheduler
from client.load_generator import run_load_test

def main():
    workers = [GPUWorker(i) for i in range(NUM_WORKERS)]

    load_balancer = LoadBalancer(workers)
    scheduler = Scheduler(load_balancer)

    print("Starting project test...")
    print(f"Mode: {MODE}")
    print(f"Users: {NUM_USERS}")
    print(f"Workers: {NUM_WORKERS}")
    print("-" * 40)

    start = time.time()

    results = run_load_test(
        scheduler=scheduler,
        num_users=NUM_USERS,
        max_threads=MAX_THREADS
    )

    total_time = time.time() - start
    avg_latency = sum(r.latency for r in results) / len(results)
    throughput = len(results) / total_time

    print("\nFINAL RESULTS")
    print("-" * 40)
    print(f"Mode: {MODE}")
    print(f"Total requests: {len(results)}")
    print(f"Workers used: {NUM_WORKERS}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Average latency: {avg_latency:.2f}s")
    print(f"Throughput: {throughput:.2f} requests/second")

    print("\nWORKER DISTRIBUTION")
    print("-" * 40)

    for worker_id in range(NUM_WORKERS):
        count = sum(1 for r in results if r.worker_id == worker_id)
        print(f"Worker {worker_id}: {count} requests")

    print("\nSAMPLE ANSWER")
    print("-" * 40)
    print(results[0].result)

if __name__ == "__main__":
    main()