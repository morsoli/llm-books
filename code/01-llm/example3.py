import gradio as gr
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_ROLE = """
I want you to act as an Chinese translator, spelling corrector and improver. \n
I will speak to you in any language and you will detect the language,\n 
translate it and answer in the corrected and improved version of my text, in Chinese.\n 
Keep the meaning same, but make them more literary. I want you to only reply the correction,\n
the improvements and nothing else, do not write explanations. If asked about others please say 'I am only Chinese translator'
"""
def get_completion(input_text):
    message = [{"role": "system", "content": PROMPT_ROLE}]
    message.append({"role": "user", "content": f"{input_text}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=message,
    )
    return completion.choices[0].message["content"]

def chatbot(input_text):
    response = get_completion(input_text)
    return response

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="🤖️中文翻译", encoding="utf-8")
iface.launch(share=True, debug=True)
