# muscleCellAtlas
The muscleCellAtlas project is a Jupyter Lab-based project for analyzing muscle cell data, including gene expressions and cell types.
<img src="https://skillicons.dev/icons?i=python" />

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)
5. [Contact](#contact)

## Overview
The muscleCellAtlas project is designed to analyze muscle cell data, including gene expressions and cell types, utilizing Jupyter Lab.

## Installation
To install and run the project, follow these steps:
```bash
# Build the Docker image
docker build -t musclecellatlas ./container
# Run a container from the image
docker run -p 8850:8850 musclecellatlas
```
Make sure to replace the `./container` path with the actual path to the Dockerfile if necessary.

## Usage
To access the project, visit [http://localhost:8850](http://localhost:8850) in your web browser. You may need to use the `JUPYTER_TOKEN` and `NB_USER` environment variables to authenticate and authorization.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](https://github.com/GuerreroVazquez/muscleCellAtlas/blob/main/LICENSE) file for more details.

## Contact
For any questions or feedback, please reach out to:
- **Email**: [GuerreroVazquez@gmail.com](mailto:GuerreroVazquez@gmail.com)
- **GitHub Profile**: [GuerreroVazquez](https://github.com/GuerreroVazquez)
- **LinkedIn**: [GuerreroVazquez](https://www.linkedin.com/in/kguerrerovazquez)
Feel free to open an issue on GitHub or contact me in any way if you have any queries or suggestions.
