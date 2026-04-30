from common.config import MODE

def retrieve_context(query):
    if MODE == "normal":
        return "."

    return "Load balancing distributes requests across multiple worker nodes."