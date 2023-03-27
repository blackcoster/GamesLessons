import arcade
import arcade.gui

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,600,'privet',resizable=True)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.box = arcade.gui.UIBoxLayout()

        knopka = arcade.gui.UIFlatButton(text = 'Flat Button',width=200)
        self.box.add(knopka.with_space_around(bottom=20))

        @knopka.event('on_click')
        def on_click_knopka(event):
            print('Кнопка \'knopka\' нажата')

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                child=self.box
            )
        )

        texture = arcade.load_texture(':resources:onscreen_controls/flat_dark/play.png')
        ui_texture_button = arcade.gui.UITextureButton(texture=texture)

        @ui_texture_button.event('on_click')
        def on_click_texture_button(event):
            print('текстурная кнопка нажата')

        self.box.add(ui_texture_button.with_space_around(bottom=20))

        ui_text_label = arcade.gui.UITextArea(
            text = 'Пример',
            width=250,
            height = 40,
            font_size=24,
            font_name='Kenney Future'
        )
        self.box.add(ui_text_label.with_space_around(bottom=0))

        text = 'Это текст внутри виджета'
        ui_text_label = arcade.gui.UITextArea(
            text=text,
            width=450,
            height=40,
            font_size=12,
            font_name='Arial'
        )
        self.box.add(ui_text_label.with_space_around(bottom=0))

    def on_draw(self):
        self.clear()
        self.manager.draw()

window = MyWindow()
arcade.run()