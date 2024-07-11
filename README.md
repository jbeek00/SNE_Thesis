Welcome!
This repo corresponds to the SNE Master Thesis paper titled 'Evaluating Implementations of Middleware for Distributed Simulations'.

The purpose of this repository is to provide the scripts that were used in the experimental runs of the research paper. Some notes on the files you'll find here:
- vm_welcome_basket contains shell scripts that will download necessary packages to get the vm up and running, regardless of producer or subscriber roles. init is the first script to run. The rest of the scripts are to be run before using that specific service. Pulsar.sh for example will get the necessary Pulsar packages and source installed as well as initializing/activating a virtual Python environment to run the scripts in.
- The experiments were run on a debian based OS (Ubuntu 24). If you're running a different distro, pay attention to what package is specified in the script. Replace the necessary links with your host's OS.
- RabbitMQ files have fields for authentication where username and passwords are written as function parameters in plaintext. Take cautious with this, secure files properly.
- Kafka makes use of external servies to do performance monitoring. jmxterm was used in my case, but additional options exist. jmxterm.properties needs to be newly created and added to the Kafka source code bin files. I added mine as an example, along with the .jar install file. Initially obtained from https://docs.cyclopsgroup.org/jmxterm.
