# JMI_O4550_Pipeline

This is the source code for our JMI primitive on the seed data O4550.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jmi4550 ./

Then, you can run the pipeline script in the following way:

docker run jmi4550 python O4550_JMI_wrapper.py

The output is the selected features stored in a csv file
