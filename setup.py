from setuptools import setup




with open("README.md", "r") as fh:
    long_description = fh.read()




setup(name='email_pdf',
      version='1.4',
      author="Vasu Gupta(vg)",
      description='Sending pdf document through gmail using python ',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['email_pdf'],classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],zip_safe=False)


