FROM keyi/python2-mcr2017a-rpi-isl

COPY JMI_O4550/ ./JMI_O4550
COPY setup.py ./
COPY O4550_JMI_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
