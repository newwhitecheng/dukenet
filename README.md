# mb3plus
a better mb3 implementation for DSP

## model description
It's adapted from original MobileNetV3. We add the following modifications for competition.
+ Remove all of the ‘fancy’ activations (e.g. Hard swish, ReLU6) which may either incompatible with hardware or induce significant accuracy drop after quantization.
+ Replace 5x5 depthwise separable convolutions with their 3x3 counterparts as they are not supported by the NNAPI.
+ Remove the final FC layer to reduce the number of parameters.
+ Scale up the model by 1.4x to fully utilize the given computation budget.

## Version
**Alpha Release (10/17)**
+ model name: mb3plus_v1.0.tflite.

## team information
+ team name: foreverDuke
+ team member: Tunhou Zhang, Shiyu Li, Hsin-Pai Cheng

