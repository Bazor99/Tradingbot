from setuptools import find_packages, setup 

setup(
    name="AI Trading Bot",
    version="0.0.0",
    author="Kingsley Odenigbo",
    author_email="k1ngx13y@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]      
)