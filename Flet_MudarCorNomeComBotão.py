import flet as ft

def main(page: ft.Page):
    # Função para atualizar a exibição do nome
    def exibir_nome(e):
        lbl_nome.value = txt_nome.value
        lbl_nome.color = "black"  # Cor padrão
        page.update()

    # Função para alterar a cor do nome
    def mudar_cor(e):
        if e.control.text == "Vermelho":
            lbl_nome.color = "red"
        elif e.control.text == "Azul":
            lbl_nome.color = "blue"
        elif e.control.text == "Verde":
            lbl_nome.color = "green"
        page.update()

    # Elementos da interface
    txt_nome = ft.TextField(label="Digite seu nome:", width=300)
    btn_exibir = ft.ElevatedButton("Exibir Nome", on_click=exibir_nome)

    # Botões de cores
    btn_vermelho = ft.ElevatedButton("Vermelho", on_click=mudar_cor)
    btn_azul = ft.ElevatedButton("Azul", on_click=mudar_cor)
    btn_verde = ft.ElevatedButton("Verde", on_click=mudar_cor)

    lbl_nome = ft.Text(value="", size=30)

    # Adiciona os elementos na página
    page.add(
        txt_nome,
        btn_exibir,
        lbl_nome,
        ft.Row([btn_vermelho, btn_azul, btn_verde], alignment=ft.MainAxisAlignment.CENTER),
    )

# Inicializa o app
ft.app(target=main)
