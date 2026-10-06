import easygui

nome = easygui.enterbox("Qual é o seu nome?")

if nome:
    easygui.msgbox(f"Olá, {nome}!")