from setuptools import setup, find_packages

setup(
    name="mcp-gitlab-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastmcp",
        "pydantic",
        "python-gitlab",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "mcp-gitlab=mcp_gitlab_tools.server:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="MCP server for GitLab merge request management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kitlabcode/mcp-gitlab-tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 