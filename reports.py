#!/usr/bin/env python3

from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_custom_report(pdf_file, report_title, additional_info):
    """
    This script generates a custom PDF report with a specified title and additional information.
    :param pdf_file: The output PDF file.
    :param report_title: The title for the PDF report.
    :param additional_info: Additional information to include in the report.
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(pdf_file)
    report_title = Paragraph(report_title, styles['h1'])
    report_info = Paragraph(additional_info, styles['BodyText'])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_info, empty_line])

if __name__ == '__main__':
    # Specify the PDF file name for the report
    pdf_file_name = 'custom_report.pdf'
    
    # Define the report title
    report_title = 'Custom Report Title'
    
    # Add custom information to the report
    additional_information = """
    This is a custom PDF report generated with Python.
    It can be customized with various elements like text, images, and styling.
    Customize it further to meet your specific needs.
    """
    
    # Generate the custom report
    generate_custom_report(pdf_file_name, report_title, additional_information)
