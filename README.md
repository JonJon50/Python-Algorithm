# Python Version Comparison Algorithm

## Overview

This project implements a Python algorithm to compare software version strings stored in a custom version format. The algorithm takes two version strings as input and determines if one version is less than, equal to, or greater than the other. The project includes test cases to validate the functionality of the algorithm.

## Custom Version Format

The software versions are stored as strings in a custom format with up to 5 parts: `[major].[minor].[patch].[build].[compilation]`. Each part is a non-negative integer, and periods are used solely as separators (they do not represent decimal points). Examples of version strings include:

- `2`
- `1.5`
- `2.12.4.0.6`

## Algorithm Details

The algorithm compares two version strings by splitting them into their constituent parts and comparing each part from left to right. If one part is greater than the corresponding part in the other version, the algorithm returns `1` (indicating the first version is greater). If it is smaller, the algorithm returns `-1`. If all parts are equal, the algorithm returns `0`.

### Input

- **version1**: The first version string (e.g., `"2.1"`).
- **version2**: The second version string (e.g., `"2.0.0"`).

### Output

The function returns:
- `-1` if `version1` is less than `version2`
- `0` if `version1` is equal to `version2`
- `1` if `version1` is greater than `version2`


### Usage
1. Clone the repository to your local machine.
2. Open the project in your favorite Python IDE (e.g., Visual Studio Code).
3. Run the app.py file to execute the version comparison algorithm.
4. Run the tests using the test_version_compare() function.

<br>
<h2 id="credits">Collaborators/Creditors 🏆</h2>

👨‍💻 We are Coding BootCamp Alumni of [UCF](https://www.ucf.edu/students/)  ⭐️


- [Profile]( https://github.com/JonJon50  " John Hagens ") -- John Hagens