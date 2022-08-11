from copy import deepcopy

PACKAGE_INFO = {
    "info": {
        "author": "The Python Packaging Authority",
        "author_email": "pypa-dev@googlegroups.com",
        "bugtrack_url": "",
        "classifiers": [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Software Development :: Build Tools"
        ],
        "description": "Sample project description",
        "description_content_type": None,
        "docs_url": None,
        "download_url": "UNKNOWN",
        "downloads": {
            "last_day": -1,
            "last_month": -1,
            "last_week": -1
        },
        "home_page": "https://github.com/pypa/sampleproject",
        "keywords": "sample setuptools development",
        "license": "MIT",
        "maintainer": None,
        "maintainer_email": None,
        "name": "sampleproject",
        "package_url": "https://pypi.org/project/sampleproject/",
        "platform": "UNKNOWN",
        "project_url": "https://pypi.org/project/sampleproject/",
        "project_urls": {
            "Download": "UNKNOWN",
            "Homepage": "https://github.com/pypa/sampleproject"
        },
        "release_url": "https://pypi.org/project/sampleproject/1.2.0/",
        "requires_dist": None,
        "requires_python": None,
        "summary": "A sample Python project",
        "version": "1.2.0",
        "yanked": False,
        "yanked_reason": None
    },
    "last_serial": 1591652,
    "releases": {
        "1.0": [],
        "1.2.0": [
            {
                "comment_text": "",
                "digests": {
                    "md5": "bab8eb22e6710eddae3c6c7ac3453bd9",
                    "sha256": "7a7a8b91086deccc54cac8d631e33f6a0e232ce5775c6be3dc44f86c2154019d"
                },
                "downloads": -1,
                "filename": "sampleproject-1.2.0-py2.py3-none-any.whl",
                "has_sig": False,
                "md5_digest": "bab8eb22e6710eddae3c6c7ac3453bd9",
                "packagetype": "bdist_wheel",
                "python_version": "2.7",
                "size": 3795,
                "upload_time_iso_8601": "2015-06-14T14:38:05.093750Z",
                "url": "https://files.pythonhosted.org/packages/30/52/547eb3719d0e872bdd6fe3ab60cef92596f95262e925e1943f68f840df88/sampleproject-1.2.0-py2.py3-none-any.whl",
                "yanked": False,
                "yanked_reason": None
            },
            {
                "comment_text": "",
                "digests": {
                    "md5": "d3bd605f932b3fb6e91f49be2d6f9479",
                    "sha256": "3427a8a5dd0c1e176da48a44efb410875b3973bd9843403a0997e4187c408dc1"
                },
                "downloads": -1,
                "filename": "sampleproject-1.2.0.tar.gz",
                "has_sig": False,
                "md5_digest": "d3bd605f932b3fb6e91f49be2d6f9479",
                "packagetype": "sdist",
                "python_version": "source",
                "size": 3148,
                "upload_time_iso_8601": "2015-06-14T14:37:56Z",
                "url": "https://files.pythonhosted.org/packages/eb/45/79be82bdeafcecb9dca474cad4003e32ef8e4a0dec6abbd4145ccb02abe1/sampleproject-1.2.0.tar.gz",
                "yanked": False,
                "yanked_reason": None
            }
        ]
    },
    "urls": [
        {
            "comment_text": "",
            "digests": {
                "md5": "bab8eb22e6710eddae3c6c7ac3453bd9",
                "sha256": "7a7a8b91086deccc54cac8d631e33f6a0e232ce5775c6be3dc44f86c2154019d"
            },
            "downloads": -1,
            "filename": "sampleproject-1.2.0-py2.py3-none-any.whl",
            "has_sig": False,
            "md5_digest": "bab8eb22e6710eddae3c6c7ac3453bd9",
            "packagetype": "bdist_wheel",
            "python_version": "2.7",
            "size": 3795,
            "upload_time_iso_8601": "2015-06-14T14:38:05.234526",
            "url": "https://files.pythonhosted.org/packages/30/52/547eb3719d0e872bdd6fe3ab60cef92596f95262e925e1943f68f840df88/sampleproject-1.2.0-py2.py3-none-any.whl",
            "yanked": False,
            "yanked_reason": None
        },
        {
            "comment_text": "",
            "digests": {
                "md5": "d3bd605f932b3fb6e91f49be2d6f9479",
                "sha256": "3427a8a5dd0c1e176da48a44efb410875b3973bd9843403a0997e4187c408dc1"
            },
            "downloads": -1,
            "filename": "sampleproject-1.2.0.tar.gz",
            "has_sig": False,
            "md5_digest": "d3bd605f932b3fb6e91f49be2d6f9479",
            "packagetype": "sdist",
            "python_version": "source",
            "size": 3148,
            "upload_time_iso_8601": "2015-06-14T14:37:56.000001Z",
            "url": "https://files.pythonhosted.org/packages/eb/45/79be82bdeafcecb9dca474cad4003e32ef8e4a0dec6abbd4145ccb02abe1/sampleproject-1.2.0.tar.gz",
            "yanked": False,
            "yanked_reason": None
        }
    ],
    "vulnerabilities": []
}

def generate_project_info(attribute, value):
    project_info = deepcopy(PACKAGE_INFO)
    project_info["info"][attribute] = value
    
    return project_info
    