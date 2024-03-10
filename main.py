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
                hint_text='Digite seu email',
                border='underline',
                color='white',
                prefix_icon= ft.icons.EMAIL
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=200,
                height=40,
                hint_text='Digite sua senha',
                border='underline',
                color='white',
                prefix_icon= ft.icons.LOCK,
                password= True
            ),
            padding=ft.padding.only(20,20)
        ),
        
        ft.Container(
            ft.Checkbox(
                label= 'Salvar senha',
                check_color='white'   
            ),
            padding=ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text='ENTRAR',
                width=280,
                bgcolor='#001A55'
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Text('Fazer login com',
                text_align= 'center',
                width=320),
        
        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon= ft.icons.EMAIL,
                    tooltip='Google',
                    icon_size=35
                ),
                ft.IconButton(
                    icon= ft.icons.FACEBOOK,
                    tooltip='Facebook',
                    icon_size=35
                ),   
                ft.IconButton(
                    icon= ft.icons.APPLE,
                    tooltip='Apple',
                    icon_size=35
                )                  
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.Text('Não tem uma conta?'),
                ft.TextButton('Criar uma conta')
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
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
    page.bgcolor = ft.colors.BLUE_200
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(container)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)