# Form implementation generated from reading ui file 'registro.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Registro(object):
    def setupUi(self, Registro):
        Registro.setObjectName("Registro")
        Registro.resize(585, 610)
        self.label = QtWidgets.QLabel(parent=Registro)
        self.label.setGeometry(QtCore.QRect(200, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Registro)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 90, 160, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtEntidad = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.txtEntidad.setEditable(True)
        self.txtEntidad.setObjectName("txtEntidad")
        self.verticalLayout.addWidget(self.txtEntidad)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txtFallecidos = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtFallecidos.setObjectName("txtFallecidos")
        self.verticalLayout.addWidget(self.txtFallecidos)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txtTramo = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtTramo.setObjectName("txtTramo")
        self.verticalLayout.addWidget(self.txtTramo)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtNombre.setText("")
        self.txtNombre.setObjectName("txtNombre")
        self.verticalLayout.addWidget(self.txtNombre)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.txtLatitud = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtLatitud.setObjectName("txtLatitud")
        self.verticalLayout.addWidget(self.txtLatitud)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.txtLongitud = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtLongitud.setObjectName("txtLongitud")
        self.verticalLayout.addWidget(self.txtLongitud)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.txtPR = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtPR.setObjectName("txtPR")
        self.verticalLayout.addWidget(self.txtPR)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.txtMunicipio = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtMunicipio.setObjectName("txtMunicipio")
        self.verticalLayout.addWidget(self.txtMunicipio)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.txtDepartamento = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.txtDepartamento.setObjectName("txtDepartamento")
        self.verticalLayout.addWidget(self.txtDepartamento)
        self.btnRegistrar = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.verticalLayout.addWidget(self.btnRegistrar)
        self.lblError = QtWidgets.QLabel(parent=Registro)
        self.lblError.setGeometry(QtCore.QRect(180, 560, 201, 16))
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")

        self.retranslateUi(Registro)
        QtCore.QMetaObject.connectSlotsByName(Registro)

    def retranslateUi(self, Registro):
        _translate = QtCore.QCoreApplication.translate
        Registro.setWindowTitle(_translate("Registro", "Registro"))
        self.label.setText(_translate("Registro", "Crear registro"))
        self.label_2.setText(_translate("Registro", "Entidad:"))
        self.label_3.setText(_translate("Registro", "Fallecidos:"))
        self.label_4.setText(_translate("Registro", "Tramo:"))
        self.txtTramo.setPlaceholderText(_translate("Registro", "Ej: Bogota - Zipaquira"))
        self.label_5.setText(_translate("Registro", "Nombre de la ruta:"))
        self.txtNombre.setPlaceholderText(_translate("Registro", "Ej: Ruta del Sol"))
        self.label_6.setText(_translate("Registro", "Latitud:"))
        self.label_7.setText(_translate("Registro", "Longitud:"))
        self.label_8.setText(_translate("Registro", "PR:"))
        self.label_9.setText(_translate("Registro", "Municipio:"))
        self.label_10.setText(_translate("Registro", "Departamento:"))
        self.btnRegistrar.setText(_translate("Registro", "Registrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registro = QtWidgets.QWidget()
    ui = Ui_Registro()
    ui.setupUi(Registro)
    Registro.show()
    sys.exit(app.exec())
