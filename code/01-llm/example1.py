import os
import openai
import gradio
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(input_text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": f"{input_text}"}
        ],
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
    )
    return completion.choices[0].message["content"]

def chatbot(input_text):
    response = get_completion(input_text)
    return response

iface = gradio.Interface(fn=chatbot, inputs="text", outputs="text", title="🤖️问答机器人", encoding="utf-8")
iface.launch(share=True, debug=True)
