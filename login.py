from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(368, 600)
        self.ventanaLogin = QtWidgets.QWidget(Login)
        self.ventanaLogin.setObjectName("VentanaLogin")
        self.botonIniciar = QtWidgets.QPushButton(self.ventanaLogin)
        self.botonIniciar.setGeometry(QtCore.QRect(90, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.botonIniciar.setFont(font)
        self.botonIniciar.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background:transparent;\n"
"    border: 2px solid #C61B1B\n"
"}\n"
"QPushButton:hover{\n"
"    background:#D91818;\n"
"color:black;        \n"
"    \n"
"}")
        self.botonIniciar.setObjectName("botonIniciar")
        self.botonRegistrar = QtWidgets.QPushButton(self.ventanaLogin)
        self.botonRegistrar.setGeometry(QtCore.QRect(90, 530, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.botonRegistrar.setFont(font)
        self.botonRegistrar.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background:transparent;\n"
"    border: 2px solid #C61B1B\n"
"}\n"
"QPushButton:hover{\n"
"    background:#D91818;\n"
"color:black;        \n"
"    \n"
"}")
        self.botonRegistrar.setObjectName("botonRegistrar")
        self.labeLogo = QtWidgets.QLabel(self.ventanaLogin)
        self.labeLogo.setGeometry(QtCore.QRect(110, 20, 161, 191))
        self.labeLogo.setText("")
        self.labeLogo.setPixmap(QtGui.QPixmap("../../Desktop/proyectoUnidad3/logo.png"))
        self.labeLogo.setScaledContents(True)
        self.labeLogo.setObjectName("labeLogo")
        self.labelUsuario = QtWidgets.QLabel(self.ventanaLogin)
        self.labelUsuario.setGeometry(QtCore.QRect(70, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setObjectName("labelUsuario")
        self.labelContrasenia = QtWidgets.QLabel(self.ventanaLogin)
        self.labelContrasenia.setGeometry(QtCore.QRect(70, 341, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelContrasenia.setFont(font)
        self.labelContrasenia.setObjectName("labelContrasenia")
        self.cajaUsuario = QtWidgets.QLineEdit(self.ventanaLogin)
        self.cajaUsuario.setGeometry(QtCore.QRect(70, 280, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cajaUsuario.setFont(font)
        self.cajaUsuario.setStyleSheet("QLineEdit{\n"
"background: transparent;\n"
"color:#E84040;\n"
"border:none;\n"

"border-bottom:1px solid #756D6D;\n"
"}")
        self.cajaUsuario.setObjectName("cajaUsuario")
        self.cajaContrasenia = QtWidgets.QLineEdit(self.ventanaLogin)
        self.cajaContrasenia.setGeometry(QtCore.QRect(70, 370, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cajaContrasenia.setFont(font)
        self.cajaContrasenia.setStyleSheet("QLineEdit{\n"
"background: transparent;\n"
"color:#E84040;\n"
"border:none;\n"
"border-bottom:1px solid #756D6D;\n"
"}")
        self.cajaContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cajaContrasenia.setObjectName("cajaContrasenia")
        self.labelError = QtWidgets.QLabel(self.ventanaLogin)
        self.labelError.setGeometry(QtCore.QRect(100, 430, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelError.setFont(font)
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        Login.setCentralWidget(self.ventanaLogin)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Unidad 3"))
        self.botonIniciar.setText(_translate("Login", "Iniciar Sesión"))
        self.botonRegistrar.setText(_translate("Login", "Registrarse"))
        self.labelUsuario.setText(_translate("Login", "Usuario"))
        self.labelContrasenia.setText(_translate("Login", "Contraseña"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
