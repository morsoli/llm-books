from langchain.llms.fake import FakeListLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

def define_agent():
    tools = load_tools(["python_repl"])
    responses = ["Action: Python REPL\nAction Input: print(2 + 2)", "Final Answer: 4"]
    llm = FakeListLLM(responses=responses)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    print(agent.run("whats 2 + 2"))
    

def test_cache():
    from langchain.cache import InMemoryCache
    import time
    import langchain
    from langchain.llms import OpenAI
    llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)
    langchain.llm_cache = InMemoryCache()
    s = time.perf_counter()
    llm("Tell me a joke")
    elapsed = time.perf_counter() - s
    print("\033[1m" + f"executed first in {elapsed:0.2f} seconds." + "\033[0m")
    llm("Tell me a joke")
    elapsed2 = time.perf_counter() - elapsed
    print("\033[1m" + f"executed second in {elapsed2:0.2f} seconds." + "\033[0m")
    
def test_stream():
    from langchain.llms import OpenAI
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


    llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
    resp = llm("模仿李白的风格写一首唐诗.")
    print(resp)
    
def test_token_acount():
    from langchain.llms import OpenAI
    from langchain.callbacks import get_openai_callback


    llm = OpenAI()
    with get_openai_callback() as cb:
        resp = llm.generate(["模仿李白的风格写一首唐诗."])
        print(resp.generations[0][0].text)
        print(cb)
if __name__ == "__main__":
    # test_cache()
    # test_stream()
    test_token_acount()
    
    