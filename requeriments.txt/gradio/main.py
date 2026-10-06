import gradio as gr

def saudacao(nome):
    return f"Olá, {nome}!"

app = gr.Interface(
    fn=saudacao,
    inputs="text",
    outputs="text",
    title="Meu primeiro Gradio"
)

app.launch()