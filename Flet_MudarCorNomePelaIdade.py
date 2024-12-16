import flet as ft

def main(page: ft.Page):
    # Função para atualizar a exibição do nome e a cor com base na idade
    def exibir_nome(e):
        try:
            # Obtém os valores do nome e da idade
            nome = txt_nome.value
            idade = int(txt_idade.value)

            # Define o valor e a cor do texto com base na idade
            lbl_nome.value = nome
            if idade < 18:
                lbl_nome.color = "red"  # Menor de 18
            elif idade == 18:
                lbl_nome.color = "yellow"  # Igual a 18
            else:
                lbl_nome.color = "green"  # Maior de 18
        except ValueError:
            lbl_nome.value = "Insira uma idade válida!"
            lbl_nome.color = "black"  # Cor padrão para erro

        page.update()

    # Elementos da interface
    txt_nome = ft.TextField(label="Digite seu nome:", width=300)
    txt_idade = ft.TextField(label="Digite sua idade:", width=300, keyboard_type=ft.KeyboardType.NUMBER)
    btn_exibir = ft.ElevatedButton("Exibir Nome", on_click=exibir_nome)

    lbl_nome = ft.Text(value="", size=30)

    # Adiciona os elementos na página
    page.add(
        txt_nome,
        txt_idade,
        btn_exibir,
        lbl_nome,
    )

# Inicializa o app
ft.app(target=main)
