---
layout: page
title: Research
---
<div class="post-content">
  <div class="post-content">
  <p>Table of Contents:</p>
  <ul>
    <li>
      <a href="#dataset">Dataset</a>
      <ul>
        <li>
          <a href="#ucf_101">UCF - 101</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#preprocess">Data Pre-processing</a>
    </li>
    <li>
      <a href="#models">Models</a>
      <ul>
        <li>
          <a href="#vanilla">Vanilla Convolution LSTM</a>
          <ul>
            <li>
              <a href="#input_vanilla">Input</a>
            </li>
            <li>
              <a href="#train_vanilla">Training</a>
            </li>
            <li>
              <a href="#test_vanilla">Testing</a>
            </li>
            <li>
              <a href="#problem_vanilla">Problems</a>
            </li>
            <li>
              <a href="#output_vanilla">Results</a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#conv-lstm-deconv">Convolution LSTM with Conv-Deconv layers</a>
          <ul>
            <li>
              <a href="#input_vanilla">Input</a>
            </li>
            <li>
              <a href="#train_lstm">Training</a>
            </li>
            <li>
              <a href="#test_lstm">Testing</a>
            </li>
            <li>
              <a href="#problem_lstm">Problems</a>
            </li>
            <li>
              <a href="#output_lstm">Results</a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#teacher">Teacher Enforcement</a>
        </li>
        <li>
          <a href="#gan">Generative Adversarial Network</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#output">Current Results</a>
    </li>
    <li>
      <a href="#challenges">Current Challenges</a>
    </li>
    <li>
      <a href="#future">Future Plan</a>
    </li>
  </ul>

  <p>
    <a name="dataset"></a>
  </p>
  <h2 id="dataset">Dataset</h2>
  <p>Dataset used.</p>

  <p>
    <a name="ucf_101"></a>
  </p>
  <h3 id="ucf_101">UCF - 101</h3>
  <p>UCF101 is a dataset collected from YouTube. It contains over 13,320 realistic action videos, having 101 action categories.</p>
  <p>Diversity of UCF101 is in terms of: 
    <ul>
      <li>
        Actions and diverse camera angles,
      </li>
      <li>
        Poses and object appearance,
      </li>
      <li>
        Light and illumination, and few more.
      </li>
    </ul>
  </p>
  <p>All the 101 action categories of videos are grouped into 25 different groups. The videos that belong to same group, share similar features like background, actions or actors. Each of these groups have more or less 5-7 videos of each category.</p>
  <p>The action classes are divided into following categories:
    <ul>
      <li>
        Human-Object Interaction
      </li>
      <li>
        Body-Motion Only
      </li>
      <li>
        Human-Human Interaction
      </li>
      <li>
        Playing Musical Instruments
      </li>
      <li>
        Sports
      </li>
    </ul>
  </p>
  <p>Detailed description of the dataset can be found <a href="http://crcv.ucf.edu/papers/UCF101_CRCV-TR-12-01.pdf">here.</a></p>

  <p>
    <a name="preprocess"></a>
  </p>
  <h2 id="preprocess">Data Pre-processing</h2>
  <p>"Write about Data Pre-processing."</p>

  <p>
    <a name="models"></a>
  </p>
  <h2 id="models">Models</h2>
  <p>Models Used.</p>

  <p>
    <a name="vanilla"></a>
  </p>
  <h3 id="vanilla">Vanilla Convolution LSTM</h3>
  <p>LSTM function as a human's understanding. A human persists previous knowledge and tries to understand future events with the help of previous ones. Similarly, Recurrent neural networks function this way. But the problem of long-term dependencies give rise to Long Short Term Memory networks or LSTMs.</p>

  <p>
    <a name="input_vanilla"></a>
  </p>
  <h4 id="input_vanilla">Input</h4>
  <p>Our input <code><span class="n">X</span></code> can be described as a <strong>5</strong> dimensional numpy array:
    <div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="n">X.shape = (4, 32, 64, 64, 3)</span></code></pre>
    Here,
    <code><span class="n">Batch size = 4</span></code>,
    <code><span class="n">Number of time frames = 32 </span></code>, and
    <code><span class="n">Height of image = 64</span></code>,
    <code><span class="n">Width of image = 64</span></code>,
    <code><span class="n">Number of channels = 3</span></code>.
    </div>
  </p>

  <p>
    <a name="train_vanilla"></a>
  </p>
  <h4 id="train_vanilla">Training</h4>
  <p>
    We have implemented our model using the <a href="https://www.tensorflow.org/">Tensorflow</a> library.
  </p>
  <div class="figure">
    <img src="/img/Conv_Lstm_Training.png">
    <p align="center">
      Vanilla Convolution Model Training.
    </p>
  </div>
  <p>
    As shown in the figure, <code><span class="n">I₀, I₁, ... I₃₁</span></code> are the input images to our model. The corresponding outputs are <code><span class="n">O₁, O₂, ... O₃₂</span></code>
  </p>
  <p>
    We have used tensorflow's <a href="https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss">l2 loss</a> to compute the loss for our model.
  </p>

  <p>
    <a name="test_vanilla"></a>
  </p>
  <h4 id="test_vanilla">Testing</h4>
  <div class="figure">
    <img src="/img/Conv_LSTM_Testing.png">
    <p align="center">
      Vanilla Convolution Model Testing.
    </p>
  </div>
  <p>
    If we carefully observe in the architecture of testing of our model, we can then see that the output from previous Convolution LSTM is applied to the next Convolution LSTM as an input.
  </p>

  <p>
    <a name="problem_vanilla"></a>
  </p>
  <h4 id="problem_vanilla">Problems</h4>
  <p>
    <ul>
      <li>
        The smaller capacity of this model was an issue that we faced. Hence, we planned to change the model structure. 
      </li>
      <li>
          The above model was not very successful in learning the features from direct input at every layer. We realized the model needed to be fed with feature maps instead of the raw input images at every layer. Therefore we decided to adopt a Conv-Deconvolution architecture to learn features of the image.
      </li>
    </ul>
  </p>

  <p>
    <a name="output_vanilla"></a>
  </p>
  <h4 id="output_vanilla">Results</h4>
  <div class="figure">
    <img src="/img/0_LSTM_CONV_MODEL.png">
    <p align="center">
      Tensorboard l2 loss graph.
    </p>
  </div>
  <p>
    The figure above shows the l2 loss computed on tensorboard. Also, the terminal output attached shows the figures of the loss overtime.
  </p>


  <p>
    <a name="conv-lstm-deconv"></a>
  </p>
  <h3 id="conv-lstm-deconv">Convolution LSTM with Conv-Deconv layers</h3>
  <p>We added the Convolutional and Deconvolutional layers to our existing model.</p>

  <p>
    <a name="train_lstm"></a>
  </p>
  <h4 id="train_lstm">Training</h4>

  <div class="figure">
    <img src="/img/Conv_Deconv_Train.png">
    <p align="center">
      Convolution LSTM with Conv-Deconv layers Training.
    </p>
  </div>

  <p>We constructed 4 Convolution layers before LSTM.</p>
  <p>Convolution layer <strong>details</strong> are:

    <div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="n">Conv layer 1:
      Number of output filters = 32, kernel size = [3,3]</span></code></pre>
    <pre class="highlight"><code><span class="n">Conv layer 2:
      Number of output filters = 64, kernel size = [3,3], stride = 2</span></code></pre>
    <pre class="highlight"><code><span class="n">Conv layer 3:
      Number of output filters = 128, kernel size = [3,3], stride = 2</span></code></pre>
    <pre class="highlight"><code><span class="n">Conv layer 4:
      Number of output filters = 256, kernel size = [3,3], stride = 2</span></code></pre>
    </div>
  </p>

  <p>We constructed 5 Deconvolution layers after LSTM.</p>

  <p>Deconvolution layer <strong>details</strong> are:

    <div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="n">Deconv layer 1:
      Number of output filters = 256, kernel size = [3,3]</span></code></pre>
    <pre class="highlight"><code><span class="n">Deconv layer 2:
      Number of output filters = 128, kernel size = [3,3]</span></code></pre>
    <pre class="highlight"><code><span class="n">Deconv layer 3:
      Number of output filters = 64, kernel size = [3,3], stride = 2</span></code></pre>
    <pre class="highlight"><code><span class="n">Deconv layer 4:
      Number of output filters = 32, kernel size = [3,3], stride = 2</span></code></pre>
    <pre class="highlight"><code><span class="n">Deconv layer 5:
      Number of output filters = 3, kernel size = [3,3], activation_func = tanh</span></code></pre>
    </div>
  </p>

  <p>
    <a name="test_lstm"></a>
  </p>
  <h4 id="test_lstm">Convolution LSTM with Conv-Deconv layers testing</h4>
  <div class="figure">
    <img src="/img/Conv_Deconv_Testing.png">
    <p align="center">
      Convolution LSTM with Conv-Deconv layers Testing.
    </p>
  </div>

  <p>
    <a name="output_lstm"></a>
  </p>
  <h4 id="output_lstm">Results</h4>
  <div class="figure">
    <img src="/img/1_LSTM_CONV_DECONV.png">
    <p align="center">
      Tensorboard l2 loss graph.
    </p>
  </div>


  <p>
    <a name="teacher"></a>
  </p>
  <h3 id="teacher">Teacher Enforcement</h3>
  <p>We decided to remove teacher forcing from above model during training so that each unit sums correct teacher activa- tions as input for the next iteration instead of only summing activations from incoming units.
  </p>
  <p>After training the above model, we found that the capacity of the network was not enough to make good predictions. Therefore, we increased number of Conv-Deconv layers and introduced a Batch Normalization layer.
  </p>

  <p>
    <a name="gan"></a>
  </p>
  <h3 id="gan">Generative Adversarial Network</h3>
  <p>We are currently working on the implementation and development of GAN.</p>

  <p>
    <a name="output"></a>
  </p>
  <h2 id="output">Current Results</h2>
  <p>We evaluate current results using L2 loss and observe that the loss decreases with time.</p>
  <div class="figure">
    <img src="/img/2_teacher_removed_BN.png">
    <p align="center">
      Tensorboard l2 loss graph.
    </p>
  </div>
  <div class="figure">
    <img src="/img/CURRENT_OUTPUT.png">
    <p align="center">
      Current Output.
    </p>
  </div>


  <p>
    <a name="challenges"></a>
  </p>
  <h2 id="challenges">Current Challenges</h2>
  <p>We observe that the generated frames contain a lot of random noise as well as blurring as the number of frames increase. Also,the generated frames do not represent any significant motion. We think this could be due to the fact that L2 loss may not be the best metric for our problem. It seems that the blurring of images is typical when using L2 loss.</p>
  <p>Another major challenge we are facing is that the UCF-101 dataset contains videos for a very large number of categories. This makes it difficult for the model to learn anything specific. Also, a large number of videos do not contain any significant motion across frames.</p>


  <p>
    <a name="future"></a>
  </p>
  <h2 id="future">Future Plan</h2>
  <p>Our first step of action is to change our loss function from L2 loss to something more reasonable for our task. We have identified the image gradient difference loss from <a href="https://arxiv.org/abs/1511.05440">here</a> to be a far better loss metric. 
    We are currently in the process of implementing the same for our model. 
    We are also planning on changing the input from a static image to a sequence of 4 frames to make it easier for the model to capture motion.</p>

  <p>Another major change planned is changing our model architecture to a GAN based model to see if it improves our results. We have completed coding for the generator and will complete the discriminator step soon.</p>

  <p>In the future we also plan on feeding the model with frames that are above a threshold of L2 difference to make sure there is significant motion in the time period.</p>

</div>

</div>
