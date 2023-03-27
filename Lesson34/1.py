import arcade
import arcade.gui


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        arcade.exit()

class myWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,600,'UIFlatButtom',resizable=True)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = 'center_x',
                anchor_y='center_y',
                child=self.box
            )
        )

        start_button = arcade.gui.UIFlatButton(text='Старт',width=200)
        self.box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text='Настройки',width=200)
        self.box.add(settings_button.with_space_around(bottom = 20))

        # quit_button = arcade.gui.UIFlatButton(text='Выход',width=200)
        # self.box.add(quit_button)


        quit_button = QuitButton(text = 'Выход',width = 200)
        self.box.add(quit_button)

        start_button.on_click = self.on_click_start


        @settings_button.event('on_click')
        def on_click_settings(event):
            print('Settings',event)



    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_start(self,event):
        print('Start',event)



window = myWindow()
arcade.run()
