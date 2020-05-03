setup(
    name="connpytomysql",
    version="0.0.1",
    install_requires=["pandas", "numpy", "sqlalchemy", "pymysql"],
	packages = find_packages(exclude=['contrib', 'docs', 'tests'])
)