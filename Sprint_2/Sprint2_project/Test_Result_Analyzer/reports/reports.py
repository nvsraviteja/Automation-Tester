from analyzer.analyzer import TestResultAnalyzer

class ReportWriter():
    
    def format_report(self):
        report = ""
        report += "=" * 10 + " TEST REPORT " + "=" * 10
        report += f"\nTotal Test Cases: {self.analyzer.total}"
        report += f"\nPassed Test Cases: {self.analyzer.count_pass()}"
        report += f"\nFailed Test Cases: {self.analyzer.count_fail()}"
        report += f"\nBlocked Test Cases: {self.analyzer.count_blocked()}"
        report += "\nFailed Test Case\n"
        report += "-" * 20
        report += f"\n IDs: {', '.join(self.analyzer.get_failed_ids())}"
        report += "\n" + "=" * 30
        return report
    
    def save_report(self, filename="report.txt"):
        report = self.format_report()
        with open(filename, "w") as file:
            file.write(report)

