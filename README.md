# Object Size Detection Project

This project is aimed at detecting the size of an unknown object based on the size of a known object in a given image. The known object in this context is an ArUco marker.

## Table of Contents

- [Overview](#overview)
- [Phases](#phases)
  - [Phase 1: Object Size Detection](#phase-1-object-size-detection)
  - [Phase 2: Camera Distortion Removal](#phase-2-camera-distortion-removal)
  - [Phase 3: Accuracy Assessment](#phase-3-accuracy-assessment)

## Overview

The primary goal of this project is to determine the size of an unknown object by leveraging the size information of a known object (ArUco marker) within the same image. This can have practical applications in computer vision, robotics, and object recognition.

## Phases

### Phase 1: Object Size Detection

In the initial phase, the project focuses on detecting the size of an unknown object using the size information of a known ArUco marker within the image.

![WhatsApp Image 2024-02-09 at 13 20 32_6395159a](https://github.com/Bansal2905/object-size-detection-project/assets/116954626/cd965189-42ab-44f3-938c-62c6e3be8ca4)


### Phase 2: Camera Distortion Removal

The subsequent phase involves addressing distortions present in the camera. This is achieved through camera calibration using a checkerboard pattern. Distortion removal is crucial for accurate measurements in computer vision applications.

![WhatsApp Image 2024-02-09 at 13 23 53_20ff9a73](https://github.com/Bansal2905/object-size-detection-project/assets/116954626/3de87ed3-00d1-4705-b200-529861fb035a)


### Phase 3: Accuracy Assessment

The final phase assesses whether the removal of distortions through camera calibration enhances the accuracy in determining the size of the unknown object. This phase involves a comparative analysis before and after distortion removal.

![WhatsApp Image 2024-02-09 at 13 24 09_62a80453](https://github.com/Bansal2905/object-size-detection-project/assets/116954626/29af50d5-ad9c-4246-a243-baa225766354)
