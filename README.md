# Image Summarizer and Safety Checker Tool

## Overview

This tool leverages state-of-the-art AI to provide a concise summary of any uploaded image and assess its safety by detecting inappropriate content. Built using NVIDIA AI Workbench, the project runs seamlessly on GPU systems for real-time performance, offering efficient and fast results for content moderation and media management.

![Image Summarization in Action](images/basic.png) <!-- Add a screenshot showing the image summarizer interface -->

## Features

- **Image Summarization**: Extracts key information from an image and provides a natural language summary.
- **Safety Check**: Uses AI to detect harmful or inappropriate content, including explicit images or privacy concerns.
- **Real-Time Performance**: Optimized with NVIDIA GPUs for fast processing of images and safety checks.
  
## Tech Stack

- **NVIDIA AI Workbench**: For GPU optimization and model management.
- **CLIP/BLIP models**: For accurate image summarization.
- **ResNet/EfficientNet**: For image safety detection.
- **Flask/Streamlit**: Web interface for easy user interaction.
- **Docker**: Containerization for deployment.

![Image Safety Check](images/safety.png) <!-- Add a screenshot demonstrating the safety check feature -->

## Setup

### Prerequisites

- **NVIDIA GPU** (or a cloud-based GPU system like AWS or Google Cloud).
- **CUDA and cuDNN**: Ensure your system supports NVIDIA GPUs.
- **Docker**: Required to containerize and deploy the application.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ZealExorcist/Summarization-and-identification.git
    cd yourprojectname
    ```

2. **Run the application**:
    ```bash
    python code\Image.py
    ```

3. Access the application at `http://localhost:7860` to upload an image for summarization and safety checking.

### NVIDIA AI Workbench Integration

The project is designed to work with **NVIDIA AI Workbench** for GPU acceleration. To run the project on a GPU system:

1. Set up **NVIDIA AI Workbench** following [these instructions](https://developer.nvidia.com/ai-workbench).
2. clone the required github repo for GPU execution.
3. Run the project on your **AI Workbench** setup.

## Usage

1. Upload an image.
2. Get a natural language summary of the image.
3. View a safety report, including flags for inappropriate content.

## Example Results

### Image Summarization Example
```text
Input: A multicolored chameleon.
Output: "The image features a very angry-looking lizard, possibly a cactus or a reptile pet, resting in a pink flower. The colorful pet appears to be sitting on a pedestal surrounded by a beautiful floral arrangement. The lizard could be a gecko or a chameleon, with muted colored stripes on its back and front, giving it a unique and striking appearance. Overall, the scene captures a captivating moment where the angry, colorful pet is nestled next to the vibrant flower."
```

![Example Picture](images/used.png) 

## Video Demo

[Watch the Video Demo](https://youtu.be/r9FTwqqWsW4) <!-- Link to your demo video -->

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Social Media

- **LinkedIn**: [Rohan Nayakanti](https://linkedin.com/in/rohan-nayakanti)
- **Discord**: Bumpyrohan#8800
