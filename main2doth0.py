from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from chomper import*
hitler = QApplication([])
winda = QWidget()
winda.setFixedSize(1000,500)
winda.move(0,0)
winda.setLayout
main_layout = QVBoxLayout()
up_layout = QHBoxLayout()
list_view = QListView()
up_layout.addWidget(list_view)

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')
create_button = QPushButton("Create button")
save_button = QPushButton("Зберегти")
test_start_button = QPushButton("Почати тренування")

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Неправильна відповідь №1:', txt_Wrong1)
layout_form.addRow('Неправильна відповідь №2:', txt_Wrong2)
layout_form.addRow('Неправильна відповідь №3:', txt_Wrong3)
up_layout.addLayout(layout_form)
main_layout.addLayout(up_layout)
down_LayoutH = QHBoxLayout()
down_LayoutH.addWidget(create_button)
down_LayoutH.addWidget(save_button)
main_layout.addLayout(down_LayoutH)

main_layout.addWidget(test_start_button)
winda.setLayout(main_layout)
winda.show()
hitler.exec_()