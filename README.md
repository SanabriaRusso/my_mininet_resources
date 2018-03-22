#My Mininet Resources

This is a collection of examples and other interesting or useful resources regarding Mininet.

We have been using them for SDN lessons, but also to learn how to create interesting topologies.

Feel free to contribute to this repository, as well as a mandatory update of this READEME file :)

L

##myTriangleNet.py
It uses Mininet medium level APIs to create a topology where switches are connected to form a triangle. From each vertex/switch, 2 host are connected via Ethernet.

The example assumes there is an EXTERNAL SDN CONTROLLER. So, look at the code and change the IP for this, or just replace with 127.0.0.1 to let a local SDN Controller allow ping among hosts.

###Ideas to extend it
- Incorporate details on the links, e.g.: bandwidth, error, and other.
- Incorporate CPU-limited hosts.
