"""
Conf file for snapshot directory
"""
import os

snapshot_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            'tests', 'accessibility_tests', 'snapshots', 'test_accessibility',
                            'test_accessibility', 'headless-chrome')
