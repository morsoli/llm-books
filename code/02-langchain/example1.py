from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain

def generate_template():
    template="You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # [SystemMessage(content='You are a helpful assistant that translates English to Chinese.', additional_kwargs={}), HumanMessage(content='I like Large Language Model', additional_kwargs={}, example=False)]
    final_message = chat_prompt.format_prompt(input_language="English", output_language="Chinese", text="I like Large Language Model").to_messages()
    print(final_message)
    
def generate_chat_template():
    chat = ChatOpenAI(temperature=0)
    template = "You are a helpful assistant that translates english to Chinese."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = SystemMessagePromptTemplate.from_template(
        "Hi", additional_kwargs={"name": "example_user"}
    )
    example_ai = SystemMessagePromptTemplate.from_template(
        "Argh me mateys", additional_kwargs={"name": "example_assistant"}
    )
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, example_human, example_ai, human_message_prompt]
)
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    # "我喜欢编程"
    print(chain.run("I love programming."))

if __name__ == "__main__":
    generate_chat_template()