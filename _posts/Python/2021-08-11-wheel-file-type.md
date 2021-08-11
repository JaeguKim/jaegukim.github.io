---
layout: post
title: "Wheel File Type"
date: 2021-08-11 10:54:00 +0900
categories: [Python]
---

### Different Types of Wheels

As touched on throughout this tutorial, there are several different [variations of wheels](https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels), and the wheel’s type is reflected in its filename:

- A **universal wheel** contains `py2.py3-none-any.whl`. It supports both Python 2 and Python 3 on any OS and platform. The majority of wheels listed on the [Python Wheels](https://pythonwheels.com/) website are universal wheels.
- A **pure-Python wheel** contains either `py3-none-any.whl` or `py2.none-any.whl`. It supports either Python 3 or Python 2, but not both. It’s otherwise the same as a universal wheel, but it’ll be labeled with either `py2` or `py3` rather than the `py2.py3` label.
- A **platform wheel** supports a specific Python version and platform. It contains segments indicating a specific Python version, ABI, operating system, or architecture.

The differences between wheel types are determined by which version(s) of Python they support and whether they target a specific platform. Here’s a condensed summary of the differences between wheel variations:



| Wheel Type  | Supports Python 2 and 3 | Supports Every ABI, OS, and Platform |
| ----------- | ----------------------- | ------------------------------------ |
| Universal   | ✓                       | ✓                                    |
| Pure-Python |                         | ✓                                    |
| Platform    |                         |                                      |

## [Reference](https://realpython.com/python-wheels/#different-types-of-wheels)