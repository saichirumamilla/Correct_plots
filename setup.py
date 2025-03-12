from setuptools import setup, find_packages

setup(
    name='my_plot_correction_package',
    version='0.1.0',
    description='A package for correcting plots ready for publishing',
    author='Saikeerthi',
    author_email='chsaikeerthi55@GMAIL.COM@example.com',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        # Add any other dependencies your package needs
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
