import setuptools

setuptools.setup(
    name="my_hust_hub_utils",
    version="1.0",
    author="AndyWyy",
    author_email="wuyiyang@hust.edu.cn",
    description="写着玩的一些小工具，目前有:华科校园网一键充网费小工具",
    url="https://github.com/AndyWyy/my_hust_hub_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=["pillow", "pytesseract", "pytest-runner"],
    tests_require=["pytest"],
    python_requires=">=3.6",
    test_suite="tests"
)
