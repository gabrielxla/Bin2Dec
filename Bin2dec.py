import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

def bin2dec(binario):
    inverter = binario[::-1]
    decimal = 0
    bit = []
    posicao = 0
    for i in inverter:
        bit.append(int(i)*(2**posicao))
        posicao += 1
    decimal = sum(bit)
    return decimal

class janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bin2Dec")
        self.setGeometry(100, 100, 300, 200)
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('Conversor Binário Bin2Dec')
        self.setGeometry(1000, 200, 350, 200) 
        
        
        layout = QVBoxLayout()
        
        # 1. Texto de Instrução
        self.label_instrucao = QLabel('Digite até 8 bits:', self)
        self.label_instrucao.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_instrucao.setStyleSheet("font-weight: bold; font-size: 15px;")
        layout.addWidget(self.label_instrucao)
        
        # 2. Campo de Entrada (Input)
        self.entrada = QLineEdit(self)
        self.entrada.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entrada.setMaxLength(8)
        self.entrada.setStyleSheet("""
        QLineEdit { 
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #cccccc;
            border-radius: 10px;
            padding: 8px 12px;
            font-size: 14px;
        }
        QLineEdit:focus {
            border: 2px solid #4a86c8;
            padding: 7px 11px;
            outline: none;
        }""")
        layout.addWidget(self.entrada)
        
    
        self.botao = QPushButton('Converter', self)
        self.botao.setStyleSheet(""" 
        QPushButton {
        background-color: #4a86c8;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        }
        QPushButton:hover {
            background-color: #5a96d8;
        }
        QPushButton:pressed {
            background-color: #3a76b8;}""")
        self.botao.clicked.connect(self.converter_clique)
        layout.addWidget(self.botao)
        
        
        self.label_resultado = QLabel('Resultado Decimal: ', self)
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_resultado.setStyleSheet("font-weight: bold; font-size: 15px;")
        layout.addWidget(self.label_resultado)
        
        # Aplica o layout na janela
        self.setLayout(layout)
    def converter_clique(self):
        num_binario = self.entrada.text().strip()
        
        # Validação de erro
        if not all(i in '01' for i in num_binario):
            QMessageBox.critical(self, "Erro", "Por favor, digite apenas números binários (0 e 1).")
            return
        elif num_binario == "":
            QMessageBox.information(self,"Vazio","Por favor, digite algo antes de executar.")
            
        
        else:
            resultado = bin2dec(num_binario)
            self.label_resultado.setText(f"Resultado Decimal: {resultado}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = janela()
    janela.show()
    sys.exit(app.exec())
    