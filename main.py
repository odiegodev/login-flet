import flet as ft

container = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                'Fazer Login',
                width=320,
                size=30,
                text_align='center',
                weight='w900'
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=200,
                height=40,
                hint_text="Digite seu email",
                border='underline',
                color='black',
                prefix_icon= ft.icons.EMAIL
            )
        )
        
        
    ],
    alignment= ft.MainAxisAlignment.SPACE_EVENLY
    ),
    
    
    border_radius=20,
    width=320,
    height=500,
    bgcolor='#2967F7'
)

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(container)


ft.app(target=main)