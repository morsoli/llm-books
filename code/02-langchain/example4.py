from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

def test_parse():
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template="列出五个 {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )
    model = OpenAI(temperature=0)
    _input = prompt.format(subject="大语言模型的特性")
    output = model(_input)
    print(output)
    output_parser.parse(output)



if __name__ == "__main__":
    test_parse()