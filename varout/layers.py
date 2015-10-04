#!/usr/bin/env python

import lasagne.layers
import theano.tensor as T

class VariationalDropout(lasagne.layers.Layer):
    """
    Base class for variational dropout layers, because the noise sampling
    and initialisation can be shared between type A and B.
    Inits:
        * p - initialisation of the parameters sampled for the noise 
    distribution.
        * adaptive - one of:
            * None - will not allow updates to the dropout rate
            * "layerwise" - allow updates to a single parameter controlling the 
            updates
            * "elementwise" - allow updates to a parameter for each hidden layer
            * "weightwise" - allow updates to a parameter for each weight (don't 
            think this is actually necessary to replicate)
    """
    def __init__(self, input_layer, p=0.5, adaptive=None):



    def _sample_noise(self):
        

class VariationalDropoutA(VariationalDropout):
    """
    Variational dropout layer, implementing correlated weight noise over the 
    output of a layer. Noise in this case is applied to the activations of 
    the previous layer.
    Inits:
        * p - initialisation of the parameters sampled for the noise 
    distribution.
        * 
    """

    def get_output_for(self, input, deterministic=False, *args, **kwargs):

class VariationalDropoutB(VariationalDropout):
    """
    Variational dropout layer, implementing independent weight noise, which
    means applying noise to the activations. This should be used after a 
    Lasagne layer _without_ a nonlinearity. You can specify a nonlinearity for
    this layer to apply after the noising process.
    """
    def get_output_for(self, input, deterministic=False, *args, **kwargs):

class GaussianDropout(lasagne.layers.Layer):
    """
    Replication of the Gaussian dropout of Srivastava et al. 2014 (section
    10). To use this right, similarly to the above, this has to be applied
    to the activations of the network _before the nonlinearity_. This means
    that the prior layer must have _no nonlinearity_, and then you can 
    either apply a nonlinearity in this layer or afterwards yourself.

    Uses some of the code and comments from the Lasagne GaussianNoiseLayer:
    Parameters
    ----------
    incoming : a :class:`Layer` instance or a tuple
        the layer feeding into this layer, or the expected input shape
    p : float or tensor scalar, effective dropout probability
    """
    def __init__(self, incoming, p=0.5, nonlinearity=None, **kwargs):
        super(GaussianDropout, self).__init__(incoming, **kwargs)
        self.sigma = theano.shared(
                value=np.array(np.sqrt(p/(1.-p))).astype(theano.config.floatX),
                name='alpha'
                )
        # if we get no nonlinearity, just put a non-function there
        if nonlinearity == None:
            nonlinearity = lambda x: x

    def get_output_for(self, input, deterministic=False, **kwargs):
        """
        Parameters
        ----------
        input : tensor
        output from the previous layer
        deterministic : bool
        If true noise is disabled, see notes
        """
        if deterministic or self.sigma.get_value() == 0:
            return input
        else:
            return input*_srng.normal(input.shape, avg=1.0, std=1.)*self.sigma
