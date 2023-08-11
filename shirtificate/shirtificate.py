from fpdf import FPDF


class Tshirt_canvas:
    def __init__(self, imprint):
        self.name = imprint

    def shirt_maker(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('helvetica', 'B', 60)
        # pdf.set_text_color(255, 255, 255)
        # self.get_string_width(2)
        pdf.image('shirtificate.png', w=0, h=0)
        pdf.cell(w= 0, h= 0, txt= self.name, border= 1, align= '', fill= False, link= '')
        pdf.output('output3.pdf')


def main():
    name = Tshirt_canvas(get_name())
    name.shirt_maker()


def get_name():
    name = input("Name: ")
    name = f"{name} took CS50"
    return name

if __name__ == "__main__":
    main()