# 案例1 一个接收文本输入输出的应用

import gradio as gr

# 功能实现
# def reverse_text(text):
#     return text[::-1]

def hellotoPerson(name):
    return "你好，" + name
# 界面配置
demo = gr.Interface(
    #fn=reverse_text,#调用reverse_text函数
    fn=hellotoPerson,#调用reverse_text函数
    inputs="text",#输入组件类型为文本
    outputs="text" #输出组件类型为文本
)

#启动应用
demo.launch()

