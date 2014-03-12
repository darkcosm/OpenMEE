'''
Created on Mar 12, 2014

@author: George
'''

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

import ui_imputation_results_choice_page

class ImputationResultsChoicePage(QWizardPage, ui_imputation_results_choice_page.Ui_WizardPage):
    def __init__(self, parent=None):
        super(ImputationResultsChoicePage, self).__init__(parent)
        self.setupUi(self)
        
        self.imp_results_comboBox.currentIndexChanged[int].connect(self.populate_tablewidget)
        
    def initializePage(self):
        self.imputation_choices = self.wizard().get_imputation_choices()
        
        self.imp_results_comboBox.blockSignals(True)
        self.tableWidget.blockSignals(True)
        # Populate the combo box with choice #s
        self.imp_results_comboBox.clear()
        for i in range(len(self.imputation_choices)):
            # userdata stores the index of the choice in self.imputation_choices
            self.imp_results_comboBox.addItem("Choice #{n_choice}".format(n_choice=i+1), userData=QVariant(i))
        self.imp_results_comboBox.setCurrentIndex(0)
        
        # Need source data to see which cells were None (imputed)
        self.source_data = self.wizard().get_source_data()
        
        # Populate tablewidget with values from choice
        first_cov = self.source_data.keys()[0]
        self.table_col_count = len(self.source_data.keys())
        self.table_row_count = len(self.source_data[first_cov])
        self.populate_tablewidget(0)

        self.imp_results_comboBox.blockSignals(False)
        self.tableWidget.blockSignals(False)
        
    def populate_tablewidget(self, choice_idx):
        choice = self.imputation_choices[choice_idx]
        
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(self.table_col_count)
        self.tableWidget.setRowCount(self.table_row_count)

        self.tableWidget.setHorizontalHeaderLabels([cov.get_label() for cov in choice.keys()])

        for col,cov_values_tuple in enumerate(choice.items()):
            cov, values = cov_values_tuple
            for row,x in enumerate(values):
                item = QTableWidgetItem(str(x))
                if self.source_data[cov][row] is None:
                    item.setBackground(Qt.yellow)
                self.tableWidget.setItem(row, col, item)