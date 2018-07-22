from PyQt5.QtWidgets import *
from functools import partial

### Reste à faire : division par 0

class Calculatrice(QWidget):
    
	def __init__(self):
		super(Calculatrice, self).__init__()

		# Init Window
		self.setWindowTitle('QtCalculatrice')

		self.setupUi()
		self.setupConnections()

		self.show()
        
        
### INTERFACE DE LA CALCULATRICE ###
	def setupUi(self):

		self.le_operation = QLineEdit()
		self.le_resultat = QLineEdit('0')
        # Creation de la grille, des boutons, et remplissage
		self.gridLayout = QGridLayout(self)

		self.btn_0 = QPushButton('0')
		self.btn_1 = QPushButton('1')
		self.btn_2 = QPushButton('2')
		self.btn_3 = QPushButton('3')
		self.btn_4 = QPushButton('4')
		self.btn_5 = QPushButton('5')
		self.btn_6 = QPushButton('6')
		self.btn_7 = QPushButton('7')
		self.btn_8 = QPushButton('8')
		self.btn_9 = QPushButton('9')

		self.btn_point = QPushButton('.')
		self.btn_plus = QPushButton('+')
		self.btn_moins = QPushButton('-')
		self.btn_mult = QPushButton('*')
		self.btn_div = QPushButton('/')
		self.btn_egal = QPushButton('=')
		self.btn_c = QPushButton('C')

		self.gridLayout.addWidget(self.le_operation, 0, 0, 1, 4)
		self.gridLayout.addWidget(self.le_resultat, 1, 0, 1, 4)
		self.gridLayout.addWidget(self.btn_c, 2, 0, 1, 1)
		self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)
		self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
		self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
		self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
		self.gridLayout.addWidget(self.btn_mult, 3, 3, 1, 1)
		self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
		self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)
		self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)
		self.gridLayout.addWidget(self.btn_moins, 4, 3, 1, 1)
		self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
		self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)
		self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)
		self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)
		self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)
		self.gridLayout.addWidget(self.btn_point, 6, 2, 1, 1)
		self.gridLayout.addWidget(self.btn_egal, 6, 3, 1, 1)

		self.btns_nombres = []
        # Pour chaque widget
		for i in range(self.gridLayout.count()):
			widget = self.gridLayout.itemAt(i).widget()
            # Si le widget est un bouton
			if isinstance(widget, QPushButton):
                # On fixe la taille
				widget.setFixedSize(64, 64)
                # On rempli la liste btns_nombres avec chaque bouton de chiffre
				if widget.text().isdigit():
					self.btns_nombres.append(widget)
                    
### CONNECTIONS ### 

	def setupConnections(self):
		for btn in self.btns_nombres:
			btn.clicked.connect(partial(self.btnNombrePressed, str(btn.text())))

		self.btn_point.clicked.connect(partial(self.btnNombrePressed, str(self.btn_point.text())))

		self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
		self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
		self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
		self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))

		self.btn_egal.clicked.connect(self.calculOperation)
		self.btn_c.clicked.connect(self.supprimerResultat)
        

### PRESSION DES BOUTONS : Chiffres et Opérations


	def btnNombrePressed(self, bouton):
		#Fonction activee quand l'utilisateur appuie sur un numero (0-9)

		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		if resultat == '0':
			# Si le resultat est egal a 0 on met le nombre du bouton
			# que l'utilisateur a presse dans le LineEdit resultat
			self.le_resultat.setText(bouton)
		else:
			# Si le resultat contient autre chose que zero,
			# On ajoute le texte du bouton a celui dans le LineEdit resultat
			self.le_resultat.setText(resultat + bouton)

	def btnOperationPressed(self, operation):
		
		#Fonction activee quand l'utilisateur appuie sur une touche d'operation (+, -, /, *)

		# On recupere le texte dans le LineEdit operation
		operationText = str(self.le_operation.text())
		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		# On additionne l'operation en cours avec le texte dans le resultat
		# et on ajoute a la fin le signe de l'operation qu'on a choisie
		self.le_operation.setText(operationText + resultat + operation)
		# On reset le texte du LineEdit resultat
		self.le_resultat.setText('0')

	def supprimerResultat(self):
		# Reset des deux champs lineEdit

		self.le_resultat.setText('0')
		self.le_operation.setText('')

	def calculOperation(self):
		# Quand l'utilisateur appuye sur le bouton egal : calcul de l'opération

		# On recupere le texte dans le LineEdit resultat
		resultat = str(self.le_resultat.text())

		# On ajoute le nombre actuel dans le LineEdit resultat
		# au LineEdit operation
		self.le_operation.setText(self.le_operation.text() + resultat)
		
		# On evalue le resultat de l'operation
		resultatOperation = eval(str(self.le_operation.text()))
		
		# On met le resultat final dans le LineEdit resultat
		self.le_resultat.setText(str(resultatOperation))


app = QApplication([])
fenetre = Calculatrice()
app.exec_()
