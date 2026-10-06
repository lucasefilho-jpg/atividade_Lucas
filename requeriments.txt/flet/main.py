import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro Flet"

    texto = ft.Text("Olá! Meu primeiro aplicativo!")

    def clicar(e):
        page.add(ft.Text("Você clicou!"))

    botao = ft.Button(
        content="Clique aqui",
        on_click=clicar
    )

    page.add(texto, botao)

ft.run(main)