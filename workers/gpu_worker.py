import time
from common.models import Response
from rag.retriever import retrieve_context
from llm.inference import run_llm

class GPUWorker:
    def __init__(self, worker_id):
        self.worker_id = worker_id

    def process(self, request):
        start = time.time()

        context = retrieve_context(request.query)
        result = run_llm(request.query, context)

        latency = time.time() - start

        return Response(
            id=request.id,
            result=result.strip(),
            latency=latency,
            worker_id=self.worker_id
        )