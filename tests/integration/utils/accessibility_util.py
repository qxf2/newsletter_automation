"""
This is a class object that contains the following methods
#Inject accessibility
#Run accessibility
#Write accessibility
"""

import os
from axe_selenium_python import Axe

class Accessibility_Util:
    "Methods to inject andrun Axe"
    axe_injected = False

    def inject_accessibility_test(self):
        "Inject Axe in the test"
        script_url=os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "utils", "axe.min.js"))
        self.axe = Axe(self.driver)
        self.axe.inject()

    def run_accessibility_test(self):
        "Run Axe in the test"
        return self.axe.run()

    def write_accessibility_test(self, result, file):
        "Write the accessibility test to a file"
        return self.axe.write_results(result, file) 
   