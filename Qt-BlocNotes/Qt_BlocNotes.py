# coding: utf-8
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from glob import glob

### UI de la fenetre principale : le fichier .ui est généré avec QtDesigner ###
### Conversion en python : pyuic5 fichier.ui -o fichier.py ###

class Ui_fenetrePrincipale(object):
    def setupUi(self, fenetrePrincipale):
        fenetrePrincipale.setObjectName("fenetrePrincipale")
        fenetrePrincipale.resize(662, 486)
        self.gridLayout = QtWidgets.QGridLayout(fenetrePrincipale)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_creerNote = QtWidgets.QPushButton(fenetrePrincipale)
        self.btn_creerNote.setObjectName("btn_creerNote")
        self.gridLayout.addWidget(self.btn_creerNote, 0, 0, 1, 1)
        self.btn_supprimerNote = QtWidgets.QPushButton(fenetrePrincipale)
        self.btn_supprimerNote.setObjectName("btn_supprimerNote")
        self.gridLayout.addWidget(self.btn_supprimerNote, 0, 1, 1, 1)
        self.lw_listeDeNotes = QtWidgets.QListWidget(fenetrePrincipale)
        self.lw_listeDeNotes.setObjectName("lw_listeDeNotes")
        self.gridLayout.addWidget(self.lw_listeDeNotes, 1, 0, 2, 2)
        self.te_contenuDeLaNote = QtWidgets.QTextEdit(fenetrePrincipale)
        self.te_contenuDeLaNote.setObjectName("te_contenuDeLaNote")
        self.gridLayout.addWidget(self.te_contenuDeLaNote, 1, 2, 1, 1)
        self.btn_maj = QtWidgets.QPushButton(fenetrePrincipale)
        self.btn_maj.setObjectName("btn_maj")
        self.gridLayout.addWidget(self.btn_maj, 2, 2, 1, 1)

        self.retranslateUi(fenetrePrincipale)
        QtCore.QMetaObject.connectSlotsByName(fenetrePrincipale)

    def retranslateUi(self, fenetrePrincipale):
        _translate = QtCore.QCoreApplication.translate
        fenetrePrincipale.setWindowTitle(_translate("fenetrePrincipale", "Qt Bloc-notes"))
        self.btn_creerNote.setText(_translate("fenetrePrincipale", "Créer une Note"))
        self.btn_supprimerNote.setText(_translate("fenetrePrincipale", "Supprimer la note"))
        self.btn_maj.setText(_translate("fenetrePrincipale", "Mettre à jour"))


### Variables globales ###

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(CUR_DIR, "data")

### Fonctions utilisées par les classes du programme ###

def recupererContenuNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(DATA_FOLDER, nomDeLaNote + '.txt')
    with open(cheminDeLaNote, 'r') as f:
        contenuDeLaNote = f.read()

    return contenuDeLaNote

def creerUneNote(nomDeLaNote, contenu=''):
    cheminDeLaNote = os.path.join(DATA_FOLDER, nomDeLaNote + '.txt')

    with open(cheminDeLaNote, 'w') as f:
        f.write(contenu)

    if os.path.isfile(cheminDeLaNote):
        print('La note "{}" a bien été créée'.format(nomDeLaNote))

def recupererLesNotes():
    notes = glob(DATA_FOLDER + '/*.txt')
    # os.path.splitext pour supprimer l'extension
    # -1 sur l'os.path pour supprimer le chemin et garder le nom du fichier de l'item [0]
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]
    return notes

def supprimerUneNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(DATA_FOLDER, nomDeLaNote + '.txt')

    if os.path.isfile(cheminDeLaNote):
        os.remove(cheminDeLaNote)
        print('la note "{}" a bien été supprimée'.format(nomDeLaNote))
    else:
        print('la note "{}" n\'existe pas'.format(nomDeLaNote))

### CLASSE PRINCIPALE ET CONNECTIONS UI -> Fonctions ###

class CreateurDeNote(QWidget, Ui_fenetrePrincipale):
    def __init__(self):
        super(CreateurDeNote, self).__init__()

        self.setupUi(self)
        self.recupererNotes()
        self.setupConnections()
        self.show()

    def setupConnections(self):
        self.btn_creerNote.clicked.connect(self.creerNote)
        self.lw_listeDeNotes.itemClicked.connect(self.afficherLaNote)
        self.btn_maj.clicked.connect(self.mettreAJourLaNote)
        self.btn_supprimerNote.clicked.connect(self.supprimerNote)

    def creerNote(self):
        nomDeLaNote, ok = QInputDialog.getText(self, 'Créer une note', 'Entrez le nom de la note:')
        if not ok:
            return

        creerUneNote(nomDeLaNote)
        self.recupererNotes()

    def recupererNoteSelectionnee(self):
        notesSelectionnees = self.lw_listeDeNotes.selectedItems()
        if not notesSelectionnees:
            return

        nomDeLaNote = notesSelectionnees[-1].text()
        cheminDeLaNote = os.path.join(DATA_FOLDER, nomDeLaNote + '.txt')

        return nomDeLaNote, cheminDeLaNote

    def afficherLaNote(self):
        nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
        contenuDeLaNote = recupererContenuNote(nomDeLaNote)
        self.te_contenuDeLaNote.setText(contenuDeLaNote)

    def mettreAJourLaNote(self):
        if self.recupererNoteSelectionnee() is not None:
            nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
            contenuDeLaNote = self.te_contenuDeLaNote.toPlainText()
            # petite tricherie : on réutilise la fonction de création de note qui va écraser l'ancienne
            creerUneNote(nomDeLaNote, contenuDeLaNote)
        else:
            pass

    def supprimerNote(self):
        if self.recupererNoteSelectionnee() is not None:
            nomDeLaNote, cheminDeLaNote = self.recupererNoteSelectionnee()
            supprimerUneNote(nomDeLaNote)
            self.recupererNotes()
            self.te_contenuDeLaNote.setText('')
        else:
            pass

    def recupererNotes(self):
        self.lw_listeDeNotes.clear()
        notes = recupererLesNotes()
        self.lw_listeDeNotes.addItems(notes)

### EXECUTION ###

app = QApplication([])
nc = CreateurDeNote()
app.exec_()
