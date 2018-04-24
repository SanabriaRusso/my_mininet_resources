# My Mininet Resources

This is a collection of examples and other interesting or useful resources regarding Mininet.

We have been using them for SDN lessons, but also to learn how to create interesting topologies.

Feel free to contribute to this repository, as well as a mandatory update of this READEME file :)

L

# Example scripts

## myVerySimpleNet.py
It uses Mininet medium level APIs to create a single switch topology with two nodes connected to it.

It serves as the starting point for the rest of topologies using the medium level APIs contained in this repository.

The example assumes there is an EXTERNAL SDN CONTROLLER. So, look at the code and change the IP for this, or just replace with 127.0.0.1 to let a local SDN Controller allow ping among hosts.

## myTriangleNet.py
It uses Mininet medium level APIs to create a topology where switches are connected to form a triangle. From each vertex/switch, 2 host are connected via Ethernet.

The example assumes there is an EXTERNAL SDN CONTROLLER. So, look at the code and change the IP for this, or just replace with 127.0.0.1 to let a local SDN Controller allow ping among hosts.

## myLocalSimpleNet.py
Similar to mySimpleNet.py, but this time the controller is local. That is, commands such as pingall, and others, will work because switches do not need an SDN Controller.

### Ideas to extend it
- Incorporate details on the links, e.g.: bandwidth, error, and other.
- Incorporate CPU-limited hosts.

# Topology Visualization
After building a topology, sometimes it is very useful to have a visual representation of it. This can help you debugg your code, or at least, help you understand what you are doing.

Head over to the [Mininet Topology Visualizer]. Then, you can simply execute your Mininet script and copy the output of:
```bash
mininet> dump
```
and,
```bash
mininet> links
```

, to the corresponding text holders. Clicking on "Render Graph" will draw the topology according to the supplied inputs.


[Mininet Topology Visualizer]: http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet
