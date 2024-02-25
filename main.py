from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu


class PVCalculator(MDApp):
    def menu1_open(self):
        menu_items = [
            {
                "text": "Без механизам",
                "on_release": lambda x = "Без механизам": self.callback1(x)
            },
            {
                "text": "Еднокрилен прозор",
                "on_release": lambda x="Еднокрилен прозор": self.callback1(x)
            },
            {
                "text": "Двокрилен прозор",
                "on_release": lambda x="Двокрилен прозор": self.callback1(x)
            },
            {
                "text": "Еднокрилна врата",
                "on_release": lambda x="Еднокрилна врата": self.callback1(x)
            },
            {
                "text": "Двокрилна врата",
                "on_release": lambda x="Двокрилна врата": self.callback1(x)
            }
        ]
        MDDropdownMenu(
            caller=self.root.ids.meh_button, items=menu_items
        ).open()

    def menu2_open(self):
        menu_items = [
            {
                "text": "Муштерија",
                "on_release": lambda x="Муштерија": self.callback2(x)
            },
            {
                "text": "Монтер",
                "on_release": lambda x="Монтер": self.callback2(x)
            }
        ]
        MDDropdownMenu(
            caller=self.root.ids.customer_button, items=menu_items
        ).open()

    def calculate(self):
        width = float(self.root.ids.w_input.text)
        length = float(self.root.ids.h_input.text)
        wings = int(self.root.ids.wings_input.text)
        wings_opening = int(self.root.ids.opening_input.text)
        meh = self.root.ids.meh_label.text
        customer = self.root.ids.customer_label.text

        self.root.ids.w_label.text = f"{self.root.ids.w_label.text} ({self.root.ids.w_input.text}m)"
        self.root.ids.h_label.text = f"{self.root.ids.h_label.text} ({self.root.ids.h_input.text}m)"
        self.root.ids.wings_label.text = f"{self.root.ids.wings_label.text} ({self.root.ids.wings_input.text})"
        self.root.ids.opening_label.text = f"{self.root.ids.opening_label.text} ({self.root.ids.opening_input.text})"

        total_pvc_mat = 0
        price_glass = 0

        total_pvc_mat += 4 * width + 4 * length
        price_pvc = 0
        price_meh = 0
        for i in range(2, wings + 1):
            total_pvc_mat += 3 * length

        if wings_opening != wings:
            copy_n = wings_opening
            while copy_n != wings:
                total_pvc_mat -= 2 * length
                copy_n += 1

            copy_n = wings_opening
            while copy_n != wings:
                total_pvc_mat -= (2.0 / wings) * width
                copy_n += 1

        if customer == "Муштерија (Муштерија)":
            if meh == "Механизам (Еднокрилен прозор)":
                price_meh = 20
            elif meh == "Механизам (Двокрилен прозор)":
                price_meh = 35
            elif meh == "Механизам (Еднокрилна врата)":
                price_meh = 25
            elif meh == "Механизам (Двокрилна врата)":
                price_meh = 40
            elif meh == "Механизам (Без механизам)":
                price_meh = 0
            price_pvc = total_pvc_mat * 9
            price_glass = width * length * 30

        elif customer == "Муштерија (Монтер)":
            if meh == "Механизам (Еднокрилен прозор)":
                price_glass = (width - 0.2) * (length - 0.2) * 30
                price_meh = 20
            elif meh == "Механизам (Двокрилен прозор)":
                price_glass = (width - 0.3) * (length - 0.2) * 30
                price_meh = 30
            elif meh == "Механизам (Еднокрилна врата)":
                price_glass = (width - 0.2) * (length - 0.2) * 30
                price_meh = 25
            elif meh == "Механизам (Двокрилна врата)":
                price_glass = (width - 0.3) * (length - 0.2) * 30
                price_meh = 35
            elif meh == "Механизам (Без механизам)":
                price_glass = (width - 0.1) * (length - 0.1) * 30
                price_meh = 0
            price_pvc = total_pvc_mat * 7

        price = round(price_pvc + price_glass + price_meh)
        self.root.ids.price_label.text = f"{price}€"

    def callback1(self, item):
        self.root.ids.meh_label.text = f"Механизам ({item})"

    def callback2(self, item):
        self.root.ids.customer_label.text = f"Муштерија ({item})"

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Light'
        return Builder.load_file("calc.kv")


if __name__ == '__main__':
    PVCalculator().run()

    