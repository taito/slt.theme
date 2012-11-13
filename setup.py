from setuptools import find_packages
from setuptools import setup


setup(
    name='slt.theme',
    version='0.2',
    description="Turns plone them into SLT shopping theme.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.sll.fi/kauppa',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['slt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'hexagonit.testing',
        'plone.app.theming',
        'plone.app.themingplugins',
        'plone.browserlayer',
        'setuptools',
        'slt.carousel',
        'slt.content',
        'z3c.autoinclude',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
