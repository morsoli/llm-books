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

def generate_template():
    template="You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # [SystemMessage(content='You are a helpful assistant that translates English to Chinese.', additional_kwargs={}), HumanMessage(content='I like Large Language Model', additional_kwargs={}, example=False)]
    final_message = chat_prompt.format_prompt(input_language="English", output_language="Chinese", text="I like Large Language Model").to_messages()
    print(final_message)

if __name__ == "__main__":
    generate_template()