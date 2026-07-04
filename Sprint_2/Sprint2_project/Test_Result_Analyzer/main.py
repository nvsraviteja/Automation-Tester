from models.test_case import *
from analyzer.analyzer import TestResultAnalyzer
from reports.reports import ReportWriter

if __name__ == "__main__":
    analyzer = TestResultAnalyzer(test_cases)
    summary = analyzer.generate_summary()
    report_writer = ReportWriter(summary)
    report_writer.save_report()
    print(str(summary))