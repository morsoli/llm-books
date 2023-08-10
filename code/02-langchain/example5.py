from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain, ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

def test_llmchain():
    human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template="What is a good name for a company that makes {product}?",
                input_variables=["product"],
            )
        )
    chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
    chat = ChatOpenAI(temperature=0.9)
    chain = LLMChain(llm=chat, prompt=chat_prompt_template)
    print(chain("colorful socks"))

def test_conversationchain():
    chat = ChatOpenAI(temperature=0.9, openai_api_base="https://api.fullstackllm.com/v1", openai_api_key="sk-763oj7cqOgMQKV0M813349708aA0457aBa1bDdBf2a685dD2")
    conversation = ConversationChain(
        llm=chat,
        memory=ConversationBufferMemory(),
        verbose=True
    )
    print(conversation.run("ChatGPT 是什么？"))

def test_mathchain():
    from langchain.chains import load_chain
    chain = load_chain("lc://chains/llm-math/chain.json")
    print(chain.run("2+2等于几"))
    
def test_chain_call():
    from langchain import PromptTemplate, OpenAI, LLMChain

    prompt_template = "给做 {product} 的公司起一个名字?"

    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(prompt_template)
    )
    print(llm_chain("儿童玩具"))
    print(llm_chain.run("儿童玩具"))
    llm_chain.apply([{"product":"儿童玩具"}])
    llm_chain.generate([{"product":"儿童玩具"}])
    llm_chain.predict(product="儿童玩具")

if __name__ == "__main__":
    #test_llmchain()
    test_conversationchain()
    #test_mathchain()
    # test_chain_call()