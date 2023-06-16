import os
import openai
import gradio
openai.api_key = os.getenv("OPENAI_API_KEY")

history_messages = []
def api_calling(input_text, history_conversation):
    if history_conversation:
        history_messages.extend([
			{"role": "user", "content": f"{history_conversation[-1][0]}"},
            {"role": "assistant", "content": f"{history_conversation[-1][1]}"}
		]
		)
    message = history_messages+[{"role": "user", "content": f"{input_text}"}]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",          
        messages=message,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
    )
    return completion.choices[0].message["content"]

def message_and_history(input, history):
    history = history or []
    output = api_calling(input, history)
    history.append((input, output))
    return history, history

block = gradio.Blocks(theme=gradio.themes.Monochrome())
with block:
    gradio.Markdown("""<h1><center>🤖️对话机器人</center></h1>
    """)
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder="输入你的问题")
    state = gradio.State()
    submit = gradio.Button("发送")
    submit.click(message_and_history,
          inputs=[message, state],
          outputs=[chatbot, state])
block.launch(share=True, debug=True)