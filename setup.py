from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="Sonam",
    author_email="sonamproject2025@gmail.com",
    url="https://github.com/sonamproject-2025/DDoS-Attack/blob/main/slowloris.py",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
