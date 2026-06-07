import gradio as gr

def reverse_and_count(text):
    reverse_text = text[::-1]
    length = len(text)
    return reverse_text, length

demo = gr.Interface(
    fn=reverse_and_count,
    inputs="text",
    outputs=["text", "number"],
    title="文本处理工具",
    description="输入一段文字，查看其倒序形式及字符数",
    examples=[["你好世界"],["hello world"]]
)

demo.launch()
