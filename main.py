import sys
from collections import defaultdict
import logging
from typing import Any, Dict, Tuple, List

from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QCheckBox, 
                               QFrame, QHBoxLayout, QLabel, QWidget, QMessageBox, QProgressBar)
from PySide6.QtCore import QThread, QObject, Signal

from app import Ui_MainWindow
import utils

logging.basicConfig(level=logging.ERROR, format='[%(levelname)s] - %(message)s')

class Worker(QObject):
    progress = Signal(int)
    finished = Signal(object)  # Emits a dictionary or an empty dict

    def __init__(self, *args: Any) -> None:
        """
        Initialize the worker with variable arguments.
        These arguments are passed to the utility functions.
        """
        super().__init__()
        self.args = args
    
    def export_file_data(self) -> None:
        """
        Export file data by calling export_to_docx.
        Reports progress and emits finished signal.
        """
        utils.export_to_docx(*self.args, progress_callback=self.progress.emit)
        self.finished.emit({})

    def process_file(self) -> None:
        """
        Process the PDF file to extract data.
        Uses a callback to build a result dictionary.
        Reports progress and emits finished signal with the result.
        """
        result: Dict[str, Dict[str, Dict[str, str]]] = defaultdict(dict)
        name: Any = None

        def add_to_result(key: str, value: Any) -> None:
            nonlocal name
            if key == 'name':
                name = value
            elif key == 'course' and name is not None:
                course = value[1]
                # Zip SCORE_TYPES with the remaining data to form a dictionary of scores
                result[name][course] = {key_: value_ for key_, value_ in zip(utils.SCORE_TYPES, value[2:])}
        
        utils.pdf_parser(*self.args, utils.PDF_FILTERS, utils.PDF_PATTERNS, utils.PDF_SUBSTITUTIONS, add_to_result,
                         progress_callback=self.progress.emit)
        
        # Ensure progress reaches 100% after processing
        self.progress.emit(100)
        self.finished.emit(result)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Initialize the main window, setting up the UI and connecting signals.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup status bar widgets
        self.ui.status_container = QWidget()
        self.ui.status_container_layout = QHBoxLayout(self.ui.status_container)
        self.ui.status_container_layout.setContentsMargins(9, 0, 9, 0) 
        self.ui.status_container_layout.setSpacing(8)

        self.ui.statustext = QLabel()
        self.ui.statustext.setObjectName("statustext")
        self.ui.statustext.setText('')
        self.ui.status_container_layout.addWidget(self.ui.statustext)
        
        self.ui.progress_bar = QProgressBar()
        self.ui.progress_bar.setObjectName("progress_bar")
        self.ui.status_container_layout.addWidget(self.ui.progress_bar)

        self.ui.statusbar.addWidget(self.ui.status_container, 1)

        # Initialize UI components
        self.ui.file_name.setText('No file selected')
        self.ui.process_pdf_btn.setEnabled(False)
        self.ui.progress_bar.hide()
        self.ui.course_select_widget.hide()

        # Connect buttons to their functions
        self.ui.select_file_btn.clicked.connect(self.select_file)
        self.ui.process_pdf_btn.clicked.connect(self.process_file)
        self.ui.export_as_docx_btn.clicked.connect(self.export_file_data)

        self.file_path: str | None = None
        self.progress: int = 0
    
    def set_status(self, text: str) -> None:
        """Update the status text in the status bar."""
        self.ui.statustext.setText(text)
    
    def clear_status(self) -> None:
        """Clear the status text."""
        self.ui.statustext.setText('')

    def show_error(self, message: str, submessage: str | None = None) -> None:
        """Show an error message dialog."""
        error_box = QMessageBox(self)
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        if submessage:
            error_box.setInformativeText(submessage)
        error_box.exec()
    
    def select_file(self) -> None:
        """
        Open a file dialog for selecting a PDF file.
        Resets UI components based on selection.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Open File",
            filter="PDF Files (*.pdf)"
        )

        if file_path:
            self.ui.file_name.setText(f'Selected file: {file_path.split("/")[-1]}')
            self.ui.process_pdf_btn.setEnabled(True)
            self.file_path = file_path

            self.ui.course_select_widget.hide()
            self.ui.instructions_label.show()

            # Clear any previous course checkboxes
            while self.ui.verticalLayout_11.count():
                child = self.ui.verticalLayout_11.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            
            self.ui.process_pdf_btn.setEnabled(True)

    def process_file(self) -> None:
        """
        Disable UI elements, start a separate thread to process the PDF file,
        and update the progress bar.
        """
        self.progress = 0
        self.ui.progress_bar.setValue(0)
        self.ui.progress_bar.show()
        self.set_status('Processing...')
        self.ui.select_file_btn.setEnabled(False)
        self.ui.export_as_docx_btn.setEnabled(False)
        self.ui.process_pdf_btn.setEnabled(False)
        
        self.thread = QThread()
        # Pass file_path to the worker for processing
        self.worker = Worker(self.file_path)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process_file)
        self.worker.finished.connect(self.process_file_done)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.progress.connect(self.update_progress)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
    
    def update_progress(self, progress: int) -> None:
        """
        Update progress bar value if new progress is higher than current.
        
        :param progress: The current progress percentage.
        """
        if progress > self.progress:
            self.progress = progress
            self.ui.progress_bar.setValue(self.progress)

    def process_file_done(self, result: Dict[str, Any]) -> None:
        """
        Handle the completion of PDF processing.
        Updates UI based on result or shows an error if processing failed.
        """
        if not result:
            self.ui.file_name.setText('No file selected')
            self.ui.process_pdf_btn.setEnabled(False)
            self.ui.progress_bar.hide()
            self.clear_status()
            self.ui.course_select_widget.hide()
            self.ui.instructions_label.show()
            self.ui.select_file_btn.setEnabled(True)
            self.show_error('Failed to process file!',
                            'Possible reasons:\n- PDF file does not contain any data\n- PDF File format is not supported\n- PDF file does not exist')
            return

        self.ui.instructions_label.hide()
        self.result = result
        self.ui.progress_bar.hide()
        self.clear_status()
        self.show_selected_courses()
        self.ui.course_select_widget.show()
        self.ui.select_file_btn.setEnabled(True)
        self.ui.export_as_docx_btn.setEnabled(True)
        self.ui.process_pdf_btn.setEnabled(False)
        self.adjustSize()
    
    def show_selected_courses(self) -> None:
        """
        Display checkboxes for each course and its associated score types.
        This allows users to select which scores to export.
        """
        self.checkBoxes: Dict[str, List[QCheckBox]] = defaultdict(list)
        courses = set()
        # Aggregate courses from the results
        for course in self.result.values():
            courses.update(course.keys())
        
        for course in courses:
            course_frame = QWidget()
            _layout = QHBoxLayout(course_frame)
            course_name_label = QLabel()
            course_name_label.setText(course)
            course_name_label.setWordWrap(True)

            _layout.addWidget(course_name_label)

            score_types_frame = QFrame(course_frame)
            score_types_frame.setFrameShape(QFrame.Shape.StyledPanel)
            score_types_frame.setFrameShadow(QFrame.Shadow.Raised)
            _layout_1 = QHBoxLayout(score_types_frame)

            # Create a checkbox for each score type
            for score_type in utils.SCORE_TYPES:
                checkbox = QCheckBox(score_types_frame)
                checkbox.setText(score_type)
                _layout_1.addWidget(checkbox)
                self.checkBoxes[course].append(checkbox)

            _layout.addWidget(score_types_frame)
            self.ui.verticalLayout_11.addWidget(course_frame)

    def export_file_data(self) -> None:
        """
        Gather selected courses and score types, then export the data
        into a DOCX file using a separate thread.
        """
        options: List[Tuple[str, str]] = []
        for course, checkboxes in self.checkBoxes.items():
            for checkbox in checkboxes:
                if checkbox.isChecked():
                    options.append((course, checkbox.text()))

        if not options:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "document.docx",
            filter="Docx Files (*.docx)"
        )

        if file_path:
            self.progress = 0
            self.ui.progress_bar.setValue(0)
            self.ui.progress_bar.show()
            self.set_status('Exporting...')
            self.ui.select_file_btn.setEnabled(False)
            self.ui.export_as_docx_btn.setEnabled(False)

            self.thread = QThread()
            # Pass file_path, result, and options to the worker
            self.worker = Worker(file_path, self.result, options)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.export_file_data)
            self.worker.finished.connect(self.export_file_data_done)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.progress.connect(self.update_progress)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()
    
    def export_file_data_done(self) -> None:
        """
        Handle post-export UI updates once data export is finished.
        """
        self.ui.progress_bar.hide()
        self.clear_status()
        self.ui.select_file_btn.setEnabled(True)
        self.ui.export_as_docx_btn.setEnabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
