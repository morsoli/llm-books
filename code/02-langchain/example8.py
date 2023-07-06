from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMMathChain
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent

def test_conversation_agent():
    search = GoogleSearchAPIWrapper()
    tools = [
        Tool(
            name = "Current Search",
            func=search.run,
            description="useful for when you need to answer questions about current events or the current state of the world"
        ),
    ]
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm=OpenAI(temperature=0)
    agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
    print(agent_chain.run(input="用中文回答中国人口数量"))


def test_openai_function_agent():
    from langchain.agents import initialize_agent, Tool
    from langchain.agents import AgentType
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
    search = GoogleSearchAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    tools = [
        Tool(
            name = "Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions"
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math"
        )
    ]
    #agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # print(agent.run("辜朝明在东吴证券策略年会上说了什么？"))
    print(agent.run("用中文回答美国和日本的GDP相差多少？"))
 
def test_plan_agent():
    from langchain.chat_models import ChatOpenAI
    from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
    search = GoogleSearchAPIWrapper()
    llm = OpenAI(temperature=0)
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    tools = [
        Tool(
            name = "Search",
            func=search.run,
            description="useful for when you need to answer questions about current events"
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math"
        ),
    ]
    model = ChatOpenAI(temperature=0)
    planner = load_chat_planner(model)
    executor = load_agent_executor(model, tools, verbose=True)
    agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)
    print(agent.run("用中文回答美国GDP是多少？"))
    
def test_doc_react():
    from langchain import OpenAI, Wikipedia
    from langchain.agents import initialize_agent, Tool
    from langchain.agents import AgentType
    from langchain.agents.react.base import DocstoreExplorer

    docstore = DocstoreExplorer(Wikipedia())
    tools = [
        Tool(
            name="Search",
            func=docstore.search,
            description="useful for when you need to ask with search",
        ),
        Tool(
            name="Lookup",
            func=docstore.lookup,
            description="useful for when you need to ask with lookup",
        ),
    ]

    llm = OpenAI(temperature=0, model_name="text-davinci-002")
    react = initialize_agent(tools, llm, agent=AgentType.REACT_DOCSTORE, verbose=True)
    question = "Author David Chanoff has collaborated with a U.S. Navy admiral who served as the ambassador to the United Kingdom under which President?"
    react.run(question)
    
if __name__ == "__main__":
    import langchain
    langchain.debug = True
    #test_conversation_agent()
    #test_openai_function_agent()
    #test_plan_agent()
    test_doc_react()