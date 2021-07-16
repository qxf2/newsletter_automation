import setuptools

setuptools.setup(
    name="newsletter-automation",
    version="0.1.1",
    description="Newsletter Automation Project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    maintainer='Qxf2 Services',
    maintainer_email='test@qxf2.com',
    url='https://github.com/qxf2/newsletter_automation',
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.txt","*.html","*.py"]}
)

