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
        <li>
          <a href="#aslam">Aslan</a>
        </li>
        <li>
          <a href="#vondrick">Vondrick</a>
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
          <a href="#conv-lstm-deconv">Convolution LSTM Deconvolution</a>
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
      <a href="#output">Result</a>
    </li>
  </ul>

  <p>
    <a name="dataset"></a>
  </p>
  <h2 id="dataset">Dataset</h2>
  <p>"Write about datasets used."</p>

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
    <a name="aslam"></a>
  </p>
  <h3 id="aslam">Aslan</h3>
  <p>"Write about Aslan dataset."</p>

  <p>
    <a name="vondrick"></a>
  </p>
  <h3 id="vondrick">Vondrick</h3>
  <p>"Write about Vondrick dataset."</p>

  <p>
    <a name="preprocess"></a>
  </p>
  <h2 id="preprocess">Data Pre-processing</h2>
  <p>"Write about Data Pre-processing."</p>

  <p>
    <a name="models"></a>
  </p>
  <h2 id="models">Models</h2>
  <p>"Write about Models ."</p>

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
    As shown in the figure, <code><span class="n">I₀, I₁, ... I₃₁</span></code> are the input images to our model. The corresponding output is <code><span class="n">O₁, O₂, ... O₃₂</span></code>
  </p>
  <p>
    We have used tensorflow's <a href="https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss">l2 loss</a> to compute the loss for our model.
  </p>

  <p>
    <a name="test_vanilla"></a>
  </p>
  <h4 id="test_vanilla">Testing</h4>
  <div class="figure">
    <img src="/img/Conv_Lstm_Testing.png">
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
        The smaller capacity of this model was an issue that we faced. Hence, we planned to change the model structure by adding the Convolution and Deconvolution layers above the current model.
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
  <h3 id="conv-lstm-deconv">Convolution LSTM Deconvolution</h3>
  <p>"Write about Convolution LSTM Deconvolution Model."</p>

  <p>
    <a name="teacher"></a>
  </p>
  <h3 id="teacher">Teacher Enforcement</h3>
  <p>"Write about Teacher Enforcement Model."</p>

  <p>
    <a name="gan"></a>
  </p>
  <h3 id="gan">Generative Adversarial Network</h3>
  <p>"Write about Generative Adversarial Network."</p>

  <p>
    <a name="output"></a>
  </p>
  <h2 id="output">Result</h2>
  <p>"Write about Output Obtained."</p>

</div>

</div>
