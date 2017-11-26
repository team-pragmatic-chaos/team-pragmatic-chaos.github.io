---
layout: page
title: Timeline
permalink: /timeline/
---

## Setup

- AWS setup
- Google Cloud setup
- TensorFlow tutorial
- Tensorboard tutorial
- Jekyll setup

## Data Preprocessing
- Dataset Exploration using IPython notebook
- Image Mean subtraction
- Batch generation of data
- sk-videos for frame extraction
- Time interval generation
- Video frame analysis (minimum and maximum frame checks)
- Relative file path handling of input data
- Time frame with interval selection T0, T5, ..., T32

### Challenges
- A lot of videos did not have the FFMEG header associated with them. Reading such videos causes problems.
- The number of frames in each video may differ. Coming up with a suitable start frame was a challenge.
- UCF-101 dataset contains videos from a large number of categories. Coming up with an optimal train, test, validation split.

## Conv LSTM model
- Vanilla Conv LSTM model creation
- Output sequence of images to Video
- Train and test in Tensorflow of model
- Tensorboard logging of logs
- Checkpoint save and restore model
- Bug fixes batch data reading problem fixes


## Conv Deconv LSTM model
- Tensorboard logging of images
- Validation split size decrease
- Checkpoint to save and restore from tensorflow
- Checks for tensorboard image and batch size 



### Challenges
- The results up to this stage are not promising at all.
- Trying to predict from a static image does not allow the model to learn the relative motion between frames very well. 
- This leads to blurred output as the number of frames increase.

## Conv-Deconv LSTM with Teacher Forcing
- We decided to remove teacher forcing from above model during training so that each unit sums correct teacher activations as input for the next iteration instead of only summing activations from incoming units.

## Conv-Deconv LSTM with Batch Normalization
- After training the above model, we found that the capacity
 of the network was not enough to make good predictions.
 Therefore, we increased number of Conv-Deconv layers and
 introduced a Batch Normalization layer.

### Challenges
- At this stage we observed a slight improvement in our results. The sharpness of the predictions improved over the previous approaches.
- However, the model was still not able to capture any motion between the frames. 
- Also, trying to predict future frames from a static image was proving to be extremely difficult as there are multiple possibilities to how the dynamics of a scene may change with time.
- A new approach and major changes in our model architecture were required at this point.

### Problems with Loss Function
- We observe that the generated frames contain a lot of random noise as well as blurring as the number of frames increase.
Also,the generated frames do not represent any significant motion.
- We think this could be due to the fact that L2 loss may not be the best metric for our problem. It seems that the blurring
of images is typical when using L2 loss as stated in [1]. 

## Gradient Discriminator Loss 
We use the GDL loss which calculates difference with respect to surrondings pixels to focus on local changes rather than global changes.

<img src="https://raw.githubusercontent.com/team-pragmatic-chaos/team-pragmatic-chaos.github.io/master/img/frame_selection/GDL.png">

## Problems with dataset
## Eliminate videos in UCF-101 that have no movement

## Sequence to Sequence Model

## AutoEncoder Model 

## AutoEncoder Model with Skip Connections


### Challenges

## Multi-Scale Architecture

## Generative Adversarial Networks (4 frame prediction)


## Generative Adversarial Networks (8 frame prediction)


## Benchmark and Model Evaluation


## Documentation and Presentation

## References
1. Mathieu, Michael, Camille Couprie, and Yann LeCun. ”Deep multi-scale video prediction beyond mean square error.” arXiv preprint arXiv:1511.05440 (2015).












