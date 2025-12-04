import flet as ft
import psycopg2
def main(page:ft.Page):
    # def consultar_bd(sql):
    #     # Parâmetros de conexão (substitua pelos seus valores)
    #     conn = psycopg2.connect(
    #         host="dpg-d4iclb3qkflc73b46iu0-a.oregon-postgres.render.com",  # ou o IP do servidor
    #         port="5432",       # porta padrão do PostgreSQL
    #         database="bd_jhd",  # nome do seu banco de dados
    #         user="bd_jhd_user",
    #         password="zsdNtvunCqK8yqk4e3paqUCSTyqnoLJd"
    #     )
    #     # Criar um cursor para executar comandos
    #     cursor = conn.cursor()

    #     # Executar uma consulta para selecionar todos os dados
    #     cursor.execute(sql)
    #     # Buscar todos os resultados
    #     rows = cursor.fetchall()
    #     # Imprimir os dados
    #     # Fechar o cursor e a conexão
    #     cursor.close()
    #     conn.close()
    #     return rows
    # dados_caldo_e_bebidas_bd=consultar_bd(sql="SELECT * FROM caldo_e_bebidas;")
    # dados_petisco_e_pastel_bd=consultar_bd(sql="SELECT * FROM petisco_e_pastel;")
    dados_caldo_e_bebidas=[('caldo de sururu', '18.00', 'caldo', 1),
                           ('heineken 600ml', '18.00', 'bebida', 2),
                            ('amstel 600ml', '13.00', 'bebida', 3),
                            ('devassa 600ml', '10.00', 'bebida', 4),
                            ('itaipava 600ml', '10.00', 'bebida', 5),
                            ('antártica 600ml', '15.00', 'bebida', 6),
                            ('skol 600ml', '13.00', 'bebida', 7),
                            ('refri lata', '5.00', 'bebida', 9),
                            ('refri 1 litro', '8.00', 'bebida', 10),
                            ('ice cabaré', '10.00', 'bebida', 11),
                            ('ice 51', '10.00', 'bebida', 12),
                            ('ice smirnof', '12.00', 'bebida', 13),
                            ('brahma s/álcool 350ml', '7.00', 'bebida', 14),
                            ('heineken long s/álcool', '10.00', 'bebida', 15),
                            ('água s/gás', '3.00', 'bebida', 16),
                            ('água c/gás ', '4.00', 'bebida', 17),
                            ('brahma 600ml', '13.00', 'bebida', 8)
                            ]
    dados_petisco_e_pastel=[(1, 'carne do sol', '50.00', 'petisco'),
                            (2, 'carne do sol com fritas', '70.00', 'petisco'),
                            (3, 'batata frita', '25.00', 'petisco'),
                            (4, 'tripa frita', '30.00', 'petisco'),
                            (5, 'passarinha', '25.00', 'petisco'),
                            (6, 'calabresa', '25.00', 'petisco'),
                            (7, 'calabresa', '10.00', 'pastel'),
                            (8, 'calabresa com queijo', '13.00', 'pastel'),
                            (9, 'carne', '12.00', 'pastel'),
                            (10, 'carne com queijo', '14.00', 'pastel'),
                            (11, 'frango', '10.00', 'pastel'),
                            (12, 'frango com queijo', '13.00', 'pastel'),
                            (15, 'camarão', '20.00', 'pastel'),
                            (16, 'camarão com queijo', '22.00', 'pastel'),
                            (13, 'misto parcial\r\n(carne, frango e queijo)', '15.00', 'pastel'),
                            (14, 'misto total\r\n(carne, frango, calabresa e queijo)', '18.00', 'pastel')
                            ]
    page.bgcolor = ft.Colors.BLACK
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # função para voltar a tela principal da aplicação 
    def voltar_pricipal(e):
        tela_enviar_pedido.col= 0
        tela_principal.col = 12
        page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.SHOPPING_CART,
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_700,
        foreground_color=ft.Colors.BLACK,
        focus_color=ft.Colors.YELLOW,
        on_click=mudar_tela
    )
        page.bgcolor = ft.Colors.BLACK
        page.update()
    def mensagem_confirmado(texto):
        def fechar_tela_confirmado(e):
            tela_confirmado.open = False
            tela_confirmado.update()
            page.update()
        tela_confirmado = ft.AlertDialog(
            content_padding=ft.padding.only(bottom=-10),
            open=True,
            bgcolor=ft.Colors.WHITE,
            content=ft.Container(
                width=100,
                height=300,
                padding=ft.padding.all(10), 
                content=ft.Column(
                controls=[
                    ft.Container(
                        image=ft.DecorationImage(src='confirmado.webp',fit=ft.ImageFit.FILL),
                        width=200,
                        height=150,
                        bgcolor=ft.Colors.WHITE
                    ),
                    ft.Text(value=texto.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                    ft.ElevatedButton(
                text='ok',
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
                width=300,
                on_click=fechar_tela_confirmado
            )
                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
            )
        )
        page.open(tela_confirmado)
#     # função para separar as colunas de lanches corretamente
    def coluna_nome_lanche(value,color:ft.ColorValue,bg:ft.ColorValue):
        return ft.Container(
            expand=False,
            alignment=ft.alignment.center,
            #image=ft.DecorationImage(src='fundo.webp',fit=ft.ImageFit.COVER),
            padding=ft.padding.only(left=20,right=20,top=20),
            content=ft.Row(
                #vertical_alignment=ft.MainAxisAlignment.CENTER,
                spacing=-5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        #height=50,
                        bgcolor=bg,
                        border_radius=ft.border_radius.only(bottom_left=10,top_left=10),
                        content=ft.IconButton(
                        icon=ft.Icons.ARROW_RIGHT,
                        icon_color=color,
                        icon_size=34,
                        bgcolor=ft.Colors.TRANSPARENT
                        ),
                    ),
                        ft.Text(
                            value=value.upper(),
                            color=color,
                            size=35,
                            bgcolor=bg
                            ),
                            ft.Container(
                        #height=50,
                        offset=ft.Offset(x=0.1,y=0),
                        bgcolor=bg,
                        border_radius=ft.border_radius.only(bottom_right=10,top_right=10),
                        content=ft.IconButton(
                        icon=ft.Icons.ARROW_LEFT,
                        icon_color=color,
                        icon_size=34,
                        bgcolor=ft.Colors.TRANSPARENT
                        ),
                    ),
                ]
            )
        )
#     # função para gerar os conteiner da area de select
    def opcao(nome,col):
        return ft.Container(
            #expand=True,
            col=col,
            bgcolor=ft.Colors.BLACK87,
            shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.WHITE),
            padding=ft.padding.symmetric(horizontal=10,vertical=5),
            border_radius=ft.border_radius.all(20),
            content=ft.Text(value=nome.upper(),color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER),
            on_click=scrool
        )
    # função para rolar a tela ate o item correto
    def scrool(e):
        if e.control.content.value == "PETISCO":
            tela_principal.content.controls=[
                logo,
                select,
                coluna_nome_lanche(value="petiscos",color=ft.Colors.BLACK,bg=ft.Colors.GREY_500),
                petiscos,
                coluna_nome_lanche(value='pastéis',color=ft.Colors.RED,bg=ft.Colors.BLACK),
                pasteis,
                coluna_nome_lanche(value='caldos',color=ft.Colors.WHITE,bg=ft.Colors.BLACK),
                caldos,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT,bg=ft.Colors.BLACK),
                bebidas,
                footer

            ]
            tela_principal.update()
        elif e.control.content.value == "PASTEL":
             
            tela_principal.content.controls=[
                logo,
                select,
                coluna_nome_lanche(value='pastéis',color=ft.Colors.RED,bg=ft.Colors.BLACK),
                pasteis,
                coluna_nome_lanche(value="petiscos",color=ft.Colors.BLACK,bg=ft.Colors.GREY_500),
                petiscos,
                coluna_nome_lanche(value='caldos',color=ft.Colors.WHITE,bg=ft.Colors.BLACK),
                caldos,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT,bg=ft.Colors.BLACK),
                bebidas,
                footer

            ]
            tela_principal.update()
        elif e.control.content.value == "CALDO":
            tela_principal.content.controls=[
                logo,
                select,
                coluna_nome_lanche(value='caldos',color=ft.Colors.WHITE,bg=ft.Colors.BLACK),
                caldos,
                coluna_nome_lanche(value="petiscos",color=ft.Colors.BLACK,bg=ft.Colors.GREY_500),
                petiscos,
                coluna_nome_lanche(value='pastéis',color=ft.Colors.RED,bg=ft.Colors.BLACK),
                pasteis,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT,bg=ft.Colors.BLACK),
                bebidas,
                footer

            ]
            tela_principal.update()
        elif e.control.content.value == "BEBIDA":
            tela_principal.content.controls=[
                logo,
                select,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT,bg=ft.Colors.BLACK),
                bebidas,
                coluna_nome_lanche(value="petiscos",color=ft.Colors.BLACK,bg=ft.Colors.GREY_500),
                petiscos,
                coluna_nome_lanche(value='pastéis',color=ft.Colors.RED,bg=ft.Colors.BLACK),
                pasteis,
                coluna_nome_lanche(value='caldos',color=ft.Colors.WHITE,bg=ft.Colors.BLACK),
                caldos,
                footer

            ]
            tela_principal.update()
#     # função para amostrar o alert diologo de adicionar o lanche na lista
    def tela_lanche(e):
        fundo_vermelho = False
        if e.control.shadow.color == ft.Colors.RED:
            fundo_vermelho = True
        valor_lanche=e.control.content.controls[2].value
        lista = valor_lanche.split()
        numero_convertido= lista[1].replace(",",".")
        numero=float(numero_convertido)
        def fechar_tela(e):
            tela_aberta.open=False
            page.update()
        def excluir_do_carrinho(e):
            lista_string = e.control.parent.controls[0].content.value.split()
            total.spans[1].text -= float(lista_string[-1])
            total.update()
            for item in lista_lanches.content.controls:
                if item.content.controls[0].content.value == e.control.parent.controls[0].content.value:
                    lista_lanches.content.controls.remove(item)
                    lista_lanches.update()
                    break
        def adicionar_ao_carrinho(e):
            valor_reais = int(drop.value) * numero
            nome_lanche_separado = nome_lanche.value.split()
            str_subs=''
            for txt in nome_lanche_separado:
                if txt == "R$":
                    break
                else:
                    str_subs+=f'{txt} '
            total.spans[1].text += int(drop.value) * numero
            total.update()
            string=f'{drop.value} - pastel\n{str_subs}R$ {valor_reais}' if fundo_vermelho == True else f'{drop.value}-petisco\n{str_subs}R$ {valor_reais}'
            lista_lanches.content.controls.append(ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(15),
                    border_radius=ft.border_radius.all(10),
                    content=ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col=10,
                    padding=ft.padding.symmetric(vertical=10,horizontal=20),
                    content=ft.Text(value=string,size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                ),
                ft.IconButton(
                    col=2,
                    bgcolor=ft.Colors.WHITE,
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_900,
                    alignment=ft.alignment.center,
                    on_click=excluir_do_carrinho
                )
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
                ))
            lista_lanches.update()
            mensagem_confirmado(texto='pedido adicionado ao carrinho com sucesso!')
        tela_aberta = ft.AlertDialog(
            #inset_padding=ft.padding.symmetric(vertical=130),
            #content_padding=ft.padding.all(10),
            bgcolor=ft.Colors.WHITE,
                content=ft.Container(
                    width=320,
                    height=220,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                expand=False,
                                bgcolor=ft.Colors.WHITE10,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value='PASTEL:'.upper()if fundo_vermelho == True else 'PETISCO',size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                                        ft.Container(
                                            alignment=ft.alignment.top_center,
                                            content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(col=1),
                                               drop:= ft.Dropdown(color=ft.Colors.BLACK,options=[ft.dropdown.Option(text=f'{num}')for num in range(1,5)],col=3,select_icon_disabled_color=ft.Colors.BLACK,label='QTD',label_style=ft.TextStyle(color=ft.Colors.BLACK,),value=1),
                                               nome_lanche:= ft.Text(value=f'{e.control.content.controls[1].value} {e.control.content.controls[2].value}'.upper(),text_align=ft.TextAlign.LEFT,size=15,weight=ft.FontWeight.BOLD,col=8,color=ft.Colors.BLACK,),
                                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ),
                                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(
                                            text='Adicionar ao Carrinho',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=adicionar_ao_carrinho
                                        ),
                                        ft.ElevatedButton(
                                            text='voltar',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=fechar_tela
                                        )
                                    ],spacing=5
                                )
                            )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True
                    ),
                ),
                open=True
            )
        
        page.open(tela_aberta)
        page.expand = True
#     # função para mostrar a descrição da bibida ou porção e colocar na lista de pedidos.

    def tela_bebida_ou_porcao(e):
        fundo_branco = False
        if e.control.shadow.color == ft.Colors.WHITE:
            fundo_branco = True
        string_valor = e.control.content.controls[2].value
        valor_separado = string_valor.split()
        valor_solto = valor_separado[1]
        valor_float = valor_solto.replace(',','.')
        valor_float_final = float(valor_float)
        def excluir_do_carrinho(e):
            lista_string = e.control.parent.controls[0].content.value.split()
            total.spans[1].text -= float(lista_string[-1])
            total.update()
            for item in lista_lanches.content.controls:
                if item.content.controls[0].content.value == e.control.parent.controls[0].content.value:
                    lista_lanches.content.controls.remove(item)
                    lista_lanches.update()
                    break
        def fechar_tela(e):
            tela_aberta.open=False
            tela_aberta.update()
            page.update()
        def adicionar_ao_carrinho(e):
            valor_reais = int(drop.value) * valor_float_final
            total.spans[1].text += float(valor_reais)
            total.update()
            string=f"{drop.value} - CALDO\n{nome_bebida.value} R$ {valor_reais}" if fundo_branco == True else f"{drop.value} - BEBIDA\n{nome_bebida.value} R$ {valor_reais}"
            lista_lanches.content.controls.append(ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.all(15),
                    border_radius=ft.border_radius.all(10),
                    content=ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col=10,
                    padding=ft.padding.symmetric(vertical=10,horizontal=20),
                    content=ft.Text(value=string,size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(10),
                ),
                ft.IconButton(
                    col=2,
                    bgcolor=ft.Colors.WHITE,
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_900,
                    alignment=ft.alignment.center,
                    on_click=excluir_do_carrinho
                )
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
                ))
            lista_lanches.update()
            mensagem_confirmado(texto='pedido adicionada ao carrinho com sucesso!')
        tela_aberta = ft.AlertDialog(
            modal=True,
            barrier_color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
            inset_padding=ft.padding.symmetric(vertical=100),
            content_padding=ft.padding.only(bottom=10,left=10,right=10,top=20),
            bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                        controls=[
                            ft.Container(
                                expand=False,
                                width=320,
                                bgcolor=ft.Colors.WHITE10,
                                content=ft.Column(
                                    controls=[
                                       porcao_ou_bebida:= ft.Text(value='bebida'.upper() if e.control.shadow.color == ft.Colors.BLUE_ACCENT else 'caldo'.upper(),
                                                text_align=ft.TextAlign.CENTER,
                                                size=20,weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.BLACK,
                                                ),
                                                ft.Container(
                                            alignment=ft.alignment.top_center,
                                            content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(col=1),
                                               drop:= ft.Dropdown(options=[ft.dropdown.Option(text=f'{num}')for num in range(1,5)],col=3,icon=None,label='QTD',value=1,color=ft.Colors.BLACK,label_style=ft.TextStyle(color=ft.Colors.BLACK,)),
                                               nome_bebida:= ft.Text(value=f'{e.control.content.controls[1].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,col=8,color=ft.Colors.BLACK,),
                                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        ),
                                       preco:= ft.Text(value=f'preço: {e.control.content.controls[2].value}'.upper(),text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD,offset=ft.Offset(x=0,y=1.5),color=ft.Colors.BLACK,)
                                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5
                                )
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(
                                            text='Adicionar ao Carrinho',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=adicionar_ao_carrinho
                                        ),
                                        ft.ElevatedButton(
                                            text='voltar',
                                            color=ft.Colors.WHITE,
                                            bgcolor=ft.Colors.BLACK,
                                            width=320,
                                            on_click=fechar_tela
                                        )
                                    ],spacing=5
                                )
                            )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=True
                    ),
                open=True
            )
        
        page.open(tela_aberta)
#     # função para abrir a tela de fazer pedido
    def tela_fazer_pedido(e):
        if lista_lanches.content.controls == []:
            def fechar_tela_alerta(e):
                tela_alerta.open = False
                tela_alerta.update()
                page.update()
            tela_alerta = ft.AlertDialog(
                content_padding=ft.padding.only(bottom=-10),
                open=True,
                content=ft.Container(
                    width=100,
                    height=150,
                    padding=ft.padding.all(10), 
                    content=ft.Column(
                    controls=[
                        ft.Text(value='carrinho vazio, por favor adicione algum alimento ao carrinho!'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                        ft.ElevatedButton(
                    text='ok',
                    bgcolor=ft.Colors.BLACK,
                    color=ft.Colors.WHITE,
                    width=300,
                    on_click=fechar_tela_alerta
                )
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
                )
            )
            page.open(tela_alerta)
        else:
            def voltar_tela(e):
                tela.open = False
                tela.update()
                page.update()
            def mudar_endereco(e):
                if e.control.bgcolor == ft.Colors.RED:
                    e.control.bgcolor = ft.Colors.GREEN
                    e.control.update()
                    tela.content.content.controls.remove(mesa)
                    tela.content.content.controls.insert(1,endereco)
                    tela.update()
                elif e.control.bgcolor == ft.Colors.GREEN:
                    e.control.bgcolor = ft.Colors.RED
                    e.control.update()
                    tela.content.content.controls.remove(endereco)
                    tela.content.content.controls.insert(1,mesa)
                    tela.update()
            def confirmar(e):
                string_pedido = ''
                numero_mesa = ''
                if nome.content.controls[1].controls[1].value == '':
                    nome.content.controls[0].value = 'você esqueceu de colocar seu nome'.upper()
                    nome.content.controls[0].color = ft.Colors.RED
                    nome.update()
                else:
                    nome.content.controls[0] = ft.Text(value='por favor digite seu nome abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True)
                    nome.update()
                    string_pedido+=f'NOME: {nome.content.controls[1].controls[1].value}'
                if num_mesa.value == None:
                    mesa.content.controls[0].value = 'você esqueceu de selecionar o numero da mesa'.upper()
                    mesa.content.controls[0].color = ft.Colors.RED
                    mesa.update()
                else:
                    mesa.content.controls[0].value = 'selecione o numero da mesa abaixo.'.upper()
                    mesa.content.controls[0].color = ft.Colors.BLACK
                    mesa.update()
                    string_pedido +=f'\nMESA: {num_mesa.value}'
                    for item in lista_lanches.content.controls:
                        string_pedido +=f'\n{item.content.controls[0].content.value}'
                    string_pedido +=f'\nVALOR TOTAL: {total.spans[1].text}'
                def enviar_dados(e):
                    tela_confirmar_envio_dados.open = False
                    tela_confirmar_envio_dados.update()
                    page.update()
                    try:
                        dados = (f"{num_mesa.value}", string_pedido, True, False, f"{total.spans[1].text}")
                        # Conexão (use os mesmos parâmetros do seu script)
                        conn = psycopg2.connect(
                            host="dpg-d4nkrk15pdvs73cpfgq0-a.oregon-postgres.render.com",
                            port="5432",
                            database="bd_sherlon",
                            user="bd_sherlon_user",
                            password="2bgRgz6OxNX67YfCES8WlP05k6fMUvvM"
                        )
                        cursor = conn.cursor()
                        # Comando SQL
                        sql = """
                        INSERT INTO pedidos (numero_mesa, pedido, visivel, is_delete, total)
                        VALUES (%s, %s, %s, %s, %s);
                        """
                        # Executar o INSERT com os dados
                        cursor.execute(sql, dados)
                        # Confirmar a transação
                        conn.commit()
                        mensagem_confirmado(texto='pedido enviado com sucesso!')
                        total.update()
                    except psycopg2.Error as e:
                        def fechar_tela_confirmado(e):
                            tela_confirmado1.open = False
                            tela_confirmado1.update()
                            page.update()
                        tela_confirmado1 = ft.AlertDialog(
                            content_padding=ft.padding.only(bottom=-10),
                            open=True,
                            bgcolor=ft.Colors.WHITE,
                            content=ft.Container(
                                width=100,
                                height=300,
                                padding=ft.padding.all(10), 
                                content=ft.Column(
                                controls=[
                                    ft.Container(
                                        image=ft.DecorationImage(src='negado.webp',fit=ft.ImageFit.FILL),
                                        width=200,
                                        height=150,
                                        bgcolor=ft.Colors.WHITE
                                    ),
                                    ft.Text(value='erro interno ao enviar pedido por favor chame o garçon para te atender melhor'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                                    ft.ElevatedButton(
                                text='ok',
                                bgcolor=ft.Colors.BLACK,
                                color=ft.Colors.WHITE,
                                width=300,
                                on_click=fechar_tela_confirmado
                            )
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                            )
                        )
                        page.open(tela_confirmado1)
                    lista_lanches.content.controls = []
                    total.spans[1].text = 0.00
                    lista_lanches.update()
                def fechar_tela_confirmado(e):
                    tela_confirmar_envio_dados.open = False
                    tela_confirmar_envio_dados.update()
                    page.update()
                tela_confirmar_envio_dados = ft.AlertDialog(
                    content_padding=ft.padding.only(bottom=-10),
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    content=ft.Container(
                        width=100,
                        height=150,
                        padding=ft.padding.only(bottom=10,left=10,right=10,top=30), 
                        content=ft.Column(
                        controls=[
                            ft.Text(value='tem certeza que deseja finalizar o pedido?'.upper(),text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,italic=True),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                        text='não',
                        bgcolor=ft.Colors.BLACK,
                        color=ft.Colors.WHITE,
                        width=100,
                        on_click=fechar_tela_confirmado
                    ),
                    ft.ElevatedButton(
                        text='sim',
                        bgcolor=ft.Colors.BLACK,
                        color=ft.Colors.WHITE,
                        width=100,
                        on_click=enviar_dados
                    )
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            )
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                    )
                )
                if nome.content.controls[0].color == ft.Colors.BLACK and mesa.content.controls[0].color == ft.Colors.BLACK:
                    page.open(tela_confirmar_envio_dados)

            nome = ft.Container(
                #bgcolor=ft.Colors.RED,
                content=ft.Column(
                    controls=[
                        ft.Text(value='por favor digite seu nome abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                        ft.Row(
                            controls=[
                                ft.Text(value='nome:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                                ft.TextField(width=200,border=ft.InputBorder.UNDERLINE,height=40,hint_text='digite seu nome aqui.'.upper())
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            mesa = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(value='selecione o numero da mesa abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                        ft.Row(
                            controls=[
                                ft.Text(value='mesa:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                            num_mesa:= ft.Dropdown(
                                    width=80,
                                    color=ft.Colors.BLACK,
                                    select_icon=None,
                                    options=[ft.dropdown.Option(text=f'{num}') for num in range(1,11)],
                                    
                                )
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            endereco = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(value='digite o endereço da entrega abaixo.'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                    campo_endereco:= ft.Row(
                            controls=[
                                ft.Text(value='endereço:'.upper(),weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK,italic=True),
                                ft.TextField(width=200,border=ft.InputBorder.UNDERLINE,height=40,hint_text='digite seu endereço aqui.'.upper())
                            ],vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ]
                )
            )
            botoes_2 = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text='confirmar'.upper(),
                            width=600,
                            bgcolor=ft.Colors.BLACK,
                            color=ft.Colors.WHITE,
                            on_click=confirmar
                        ),
                        ft.ElevatedButton(
                            text='voltar'.upper(),
                            width=600,
                            bgcolor=ft.Colors.BLACK,
                            color=ft.Colors.WHITE,
                            on_click=voltar_tela
                        ),
                    ],spacing=5
                )
            )
            tela=ft.AlertDialog(
                open=True,
                content_padding=ft.padding.only(top=10,left=10,right=10,bottom=-10),
                content=ft.Container(
                    width=320,
                    height=300,
                    padding=ft.padding.only(top=10,left=10,right=10,bottom=10),
                    content=ft.Column(
                        controls=[
                            nome,
                            mesa,
                            botoes_2
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
                
            )
            
            page.open(tela)
    #parte de cima da aplicação ou o logo        
    logo=ft.Container(
        #expand=True,
        bgcolor=ft.Colors.BLACK,
        height=170,
        width=170,
        image=ft.DecorationImage(src='logo_1.png',fit=ft.ImageFit.CONTAIN),
        border_radius=ft.border_radius.all(200),
    )
    # area de selecionar qual as opções de pedido vai quer que apareca na tela
    select=ft.Container(
        width=800,
        content=ft.ResponsiveRow(
        controls=[
            opcao(nome='petisco',col=3),
            opcao(nome="pastel",col=3),
            opcao(nome="caldo",col=3),
            opcao(nome="bebida",col=3),
            ],height=40,expand=True
    )
    )
    # area de lanches normais
    #e.control.content.controls[1].value
    petiscos=ft.Container(
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.GREY_500,
            on_click=tela_lanche,
            scale=0.99,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
            padding=ft.padding.all(7),
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_spacing=-8,
                controls=[
                    ft.Container(
                        col=1,
                        height=30
                    ),
                    ft.Text(
                        value=item[1].upper(),
                        col=7,
                        color=ft.Colors.SCRIM,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        size=17
                        ),
                        ft.Text(
                            value=f"R$ {item[2]}".upper(),
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                            col=4,
                            size=17
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_petisco_e_pastel if f"{item[3]}" == "petisco"],
                key=lambda x: float(x[2]))
            ]
        )
    )
    pasteis=ft.Container(
        padding=ft.padding.all(10),
        content=ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_lanche,
            scale=0.99,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.RED),
            padding=ft.padding.all(7),
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_spacing=-8,
                controls=[
                    ft.Container(
                        col=1,
                        height=30
                    ),
                    ft.Text(
                        value=item[1].upper(),
                        col=7,
                        color=ft.Colors.RED,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        size=17
                        ),
                        ft.Text(
                            value=f"R$ {item[2]}".upper(),
                            color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                            weight=ft.FontWeight.BOLD,
                            col=4,
                            size=17
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_petisco_e_pastel if f"{item[3]}" == "pastel"],
                key=lambda x: float(x[2]))
            ]
        )
    )
    # area de caldos
    caldos=ft.Container(
        ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_bebida_ou_porcao,
            scale=0.98,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.WHITE),
            padding=ft.padding.symmetric(horizontal=30,vertical=10),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col=1,
                        height=30
                    ),
                    ft.Text(
                        value=item[0].upper(),
                        col=7,
                        color=ft.Colors.WHITE,
                        size=18
                            ),
                    ft.Text(
                        value=f"R$ {item[1]}",
                        col=4,
                        color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                        size=18
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_caldo_e_bebidas if f"{item[2]}" == "caldo"],
                key=lambda x: float(x[1]))
            ]
        )
    )
    # parte de bebidas da tela e eu estou reutilizando a funçao de caldos
    bebidas=ft.Container(
        ft.Column(
            controls=[
                ft.Container(
            bgcolor=ft.Colors.BLACK,
            on_click=tela_bebida_ou_porcao,
            scale=0.98,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLUE_ACCENT),
            padding=ft.padding.symmetric(horizontal=30,vertical=10),
            content=ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col=1,
                        height=30
                    ),
                    ft.Text(
                        value=item[0].upper(),
                        col=7,
                        color=ft.Colors.BLUE_ACCENT,
                        size=18
                            ),
                    ft.Text(
                        value=f"R$ {item[1]}",
                        col=4,
                        color=ft.Colors.LIGHT_GREEN_ACCENT_700,
                        size=18
                        ),
                ]
            )
        ) for item in sorted(
                [item for item in dados_caldo_e_bebidas if f"{item[2]}" == "bebida"],
                key=lambda x: float(x[1]))
            ]
        )
    )
    logo_enviar=ft.Container(
        padding=ft.padding.only(top=20,bottom=5,right=10,left=10),
        content=ft.Text(value='carrinho de alimentos'.upper(),size=30,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_900,italic=True,color=ft.Colors.BLACK)
    )

    lista_lanches = ft.Container(
        padding=ft.padding.symmetric(vertical=20,horizontal=20),
        bgcolor=ft.Colors.WHITE,
        height=300,
        expand=True,
        width=400,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            #expand=True,
            controls=[
                # ft.Container(
                #     bgcolor=ft.Colors.WHITE,
                #     padding=ft.padding.all(15),
                #     border_radius=ft.border_radius.all(10),
                #     content=ft.ResponsiveRow(
                #     controls=[
                #         ft.Container(
                #             col=10,
                #     padding=ft.padding.symmetric(vertical=10,horizontal=30),
                #     content=ft.Text(value='1x hamburguinho R$ 10,00',size=15,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                #     bgcolor=ft.Colors.WHITE,
                #     shadow=ft.BoxShadow(blur_radius=10,color=ft.Colors.BLACK),
                #     border_radius=ft.border_radius.all(10),
                # ),
                # ft.IconButton(
                #     col=2,
                #     bgcolor=ft.Colors.WHITE,
                #     icon=ft.Icons.DELETE_OUTLINE,
                #     icon_color=ft.Colors.RED_900,
                #     alignment=ft.alignment.center,
                    
                # )
                #     ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                # )
                # )  for l in range(5)
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER,spacing=0
        )
    )
    total = ft.Text(
        spans=[
            ft.TextSpan(text='valor total r$ '.upper(),style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
            ft.TextSpan(text=0.00,style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
        ]
    )
    # total.spans[1].text += 15.00
    
    # print(total.spans[1])
    botoes = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(text='fazer pedido'.upper(),width=400,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=tela_fazer_pedido),
                ft.ElevatedButton(text='voltar'.upper(),width=400,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=voltar_pricipal),
            ]
        )
    )
    footer = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    offset=ft.Offset(x=0,y=-0.03),
                    col=12,
                    url='https://wa.me/<557199407781>',
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                
                    image=ft.DecorationImage(src='whatsapp.webp',fit=ft.ImageFit.FILL),
                    width=100,
                    height=100,
                            ),
                            ft.Text(value='+55 71 999407781\nqualquer duvida chama no whatsapp!',color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=-20
                    )
                    
                ),
                # ft.Container(
                #     col=6,
                #     url='https://www.instagram.com/mamae_lanches_e_drinks_/',
                #     content=ft.Column(
                #         controls=[
                #             ft.Container(
                #                 image=ft.DecorationImage(src='instagran.webp',fit=ft.ImageFit.FILL),
                #                 width=100,
                #                 height=100,
                #             ),
                #             ft.Text(value='@mamae_lanches_e_drinks',color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
                #         ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=-15
                #     )
                    
                # ),
            ]
        )
    )
#     # tela principal da aplicação
    tela_principal=ft.Container(
        #expand=True,
        padding=ft.padding.symmetric(vertical=10),
        col=12,
        image=ft.DecorationImage(src='fundo_logo.png',fit=ft.ImageFit.FILL,),
        #width=400,
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                logo,
                select,
                coluna_nome_lanche(value="petiscos",color=ft.Colors.BLACK,bg=ft.Colors.GREY_500),
                petiscos,
                coluna_nome_lanche(value='pastéis',color=ft.Colors.RED,bg=ft.Colors.BLACK),
                pasteis,
                coluna_nome_lanche(value='caldos',color=ft.Colors.WHITE,bg=ft.Colors.BLACK),
                caldos,
                coluna_nome_lanche(value='bebidas',color=ft.Colors.BLUE_ACCENT,bg=ft.Colors.BLACK),
                bebidas,
                footer

            ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    tela_enviar_pedido = ft.Container(
        width=800,
        border_radius=ft.border_radius.all(10),
        col=0,
        padding=ft.padding.all(10),
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            #expand=True,
            width=600,
            height=600,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                logo_enviar,
                lista_lanches,
                total,
                botoes,
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    layout = ft.Container(
        expand=True,
        content=ft.ResponsiveRow(
        columns=12,
        controls=[
            tela_principal,
            tela_enviar_pedido
        ]
    )
    )
    def mudar_tela(e):
        tela_principal.col = 0
        tela_enviar_pedido.col = 12
        page.floating_action_button = None 
        page.bgcolor = ft.Colors.WHITE
        page.update()
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.SHOPPING_CART,
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_700,
        foreground_color=ft.Colors.BLACK,
        focus_color=ft.Colors.YELLOW,
        on_click=mudar_tela
    )
    page.add(layout)
if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')