"""Main module"""
#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansfortrankernel
IPKernelApp.launch_instance(kernel_class=jansfortrankernel)
