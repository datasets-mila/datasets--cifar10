import torchvision

torchvision.datasets.CIFAR10(".", train=True, download=True)
torchvision.datasets.CIFAR10(".", train=False, download=True)

