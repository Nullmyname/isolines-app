from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class IsolineApp(App):
    def build(self):
        # Устанавливаем цвет фона
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
       
        # Главный layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
       
        # Заголовок
        title = Label(
            text='[b]Расчет изолиний[/b]\nГеология и геохимия горючих ископаемых',
            size_hint=(1, 0.15),
            font_size='24sp',
            halign='center',
            markup=True
        )
       
        # Поля ввода
        input_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.3))
       
        self.input_a = TextInput(
            hint_text='Высота точки A (например: -2263.2 или -2263,2)',
            multiline=False,
            size_hint=(1, 0.3),
            font_size='18sp',
            background_color=(1, 1, 1, 1)
        )
       
        self.input_b = TextInput(
            hint_text='Высота точки B (например: -2256.8 или -2256,8)',
            multiline=False,
            size_hint=(1, 0.3),
            font_size='18sp',
            background_color=(1, 1, 1, 1)
        )
       
        self.input_l = TextInput(
            hint_text='Расстояние между точками в мм (например: 50)',
            multiline=False,
            size_hint=(1, 0.3),
            font_size='18sp',
            background_color=(1, 1, 1, 1)
        )
       
        # Кнопка расчета
        calculate_btn = Button(
            text='[b]РАССЧИТАТЬ ИЗОЛИНИИ[/b]',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.5, 0.8, 1),
            font_size='20sp',
            markup=True
        )
        calculate_btn.bind(on_press=self.calculate_isolines)
       
        # Поле результатов
        self.result_label = Label(
            text='Введите данные и нажмите "РАССЧИТАТЬ ИЗОЛИНИИ"\n\nЗдесь появится результат расчета...',
            size_hint=(1, 0.45),
            text_size=(None, None),
            halign='left',
            valign='top',
            font_size='16sp',
            color=(0, 0, 0, 1)
        )
       
        # Добавляем все в layout
        input_layout.add_widget(self.input_a)
        input_layout.add_widget(self.input_b)
        input_layout.add_widget(self.input_l)
       
        main_layout.add_widget(title)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(calculate_btn)
        main_layout.add_widget(self.result_label)
       
        return main_layout
   
    def calculate_isolines(self, instance):
        try:
            # Получаем данные из полей ввода
            a_text = self.input_a.text.strip()
            b_text = self.input_b.text.strip()
            l_text = self.input_l.text.strip()
           
            if not a_text or not b_text or not l_text:
                self.result_label.text = "Ошибка! Заполните все поля."
                return
           
            a = float(a_text.replace(',', '.'))
            b = float(b_text.replace(',', '.'))
            L = float(l_text.replace(',', '.'))
           
            if L <= 0:
                self.result_label.text = "Ошибка! Расстояние должно быть больше 0."
                return
           
            step = 20
            Ldifferent = abs(a - b)
           
            if Ldifferent == 0:
                self.result_label.text = "Точки имеют одинаковую высоту.\nИзолинии между ними отсутствуют."
                return
           
            uklon = L / Ldifferent
           
            # Находим все изолинии между точками
            min_h, max_h = min(a, b), max(a, b)
            isolines = []
           
            # Определяем первую изолинию в диапазоне
            start_iso = (int(min_h) // step) * step
            if min_h % step != 0:
                if min_h < 0:
                    start_iso -= step
                else:
                    start_iso += step
           
            current = start_iso
            while min_h <= current <= max_h:
                isolines.append(current)
                current += step
           
            # Формируем результат
            result_text = f"[b]РЕЗУЛЬТАТЫ РАСЧЕТА:[/b]\n\n"
            result_text += f"• Точка A: {a} м\n"
            result_text += f"• Точка B: {b} м\n"
            result_text += f"• Расстояние: {L} мм\n"
            result_text += f"• Уклон: {uklon:.2f} мм/м\n\n"
           
            if isolines:
                result_text += f"[b]Изолинии между точками:[/b] {isolines}\n\n"
                result_text += "[b]РАССТОЯНИЯ ОТ ТОЧКИ A:[/b]\n"
                for iso in isolines:
                    n = abs(iso - a) * uklon
                    result_text += f"• Изолиния {iso} м: {n:.2f} мм\n"
               
                if len(isolines) > 1:
                    distance_between = step * uklon
                    result_text += f"\n[b]Расстояние между соседними изолиниями:[/b]\n{distance_between:.2f} мм"
            else:
                result_text += "В указанном диапазоне изолинии отсутствуют"
           
            self.result_label.text = result_text
            self.result_label.markup = True
           
        except ValueError:
            self.result_label.text = "Ошибка! Проверьте правильность введенных данных.\n\nИспользуйте числа в формате:\n-2263.2 или -2263,2"

if __name__ == '__main__':
    IsolineApp().run()

