class CNNModelArchitecture:
    def __init__(self):
        self.layers = [
            {
                "layer": "conv2d",
                "filters": 32,
                "kernel_size": 3,
                "activation": "relu",
                "input_shape": (1, 128, 128)
            },
            {
                "layer": "max_pooling2d",
                "pool_size": 2
            },
            {
                "layer": "conv2d",
                "filters": 64,
                "kernel_size": 3,
                "activation": "relu"
            },
            {
                "layer": "max_pooling2d",
                "pool_size": 2
            },
            {
                "layer": "flatten"
            },
            {
                "layer": "dense",
                "units": 128,
                "activation": "relu"
            },
            {
                "layer": "dense",
                "units": 10,
                "activation": "softmax"
            }
        ]

    def get_layers(self):
        return self.layers
