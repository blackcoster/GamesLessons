import arcade
import arcade.gui

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,600,'okno',resizable=True)
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y = 'center_y',
                child=self.box
            )
        )

        open_message_box_button = arcade.gui.UIFlatButton(text='Open',width=200)
        self.box.add(open_message_box_button)

        open_message_box_button.on_click = self.on_click_open

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_open(self,event):
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text=('Это сообщение''Нажмите ок или cancel'),
            buttons=['ok','cancel'],
            callback=self.on_message_box_close
        )
        self.manager.add(message_box)

    def on_message_box_close(self,button):
        print(f'user pressed {button}')
        if button=='ok':
            print('ok')

        elif button=='cancel':
            arcade.exit()



window = MyWindow()
arcade.run()