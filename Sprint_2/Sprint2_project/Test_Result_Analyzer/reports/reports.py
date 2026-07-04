from analyzer.analyzer import TestResultAnalyzer

class ReportWriter():
    def __init__(self, summary):
        self.summary = summary
    
    def format_report(self):

        report = ""
        report += "=" * 10 + " TEST REPORT " + "=" * 10
        report += f"\nTotal Test Cases: {self.summary['Total']}"
        report += f"\nPassed Test Cases: {self.summary['Pass']}"
        report += f"\nFailed Test Cases: {self.summary['Fail']}"
        report += f"\nBlocked Test Cases: {self.summary['Blocked']}"
        report += "\nFailed Test Case\n"
        report += "-" * 20
        report += f"\n IDs: {', '.join(self.summary['Failed IDs'])}"
        report += "\n" + "=" * 30
        return report
    
    def save_report(self, filename="reports.txt"):
        report = self.format_report()
        with open(filename, "w") as file:
            file.write(report)

