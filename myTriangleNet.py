#!/usr/bin/python

"""
This example building a network with a Triangle Topology, where 2 hosts are connected
at each vertex. This network is controlled by an external SDN Controller.

When we say "external" we mean that the Controller is located outside Mininet's domain.
"""

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

Sw = 3 # number of switches
Nps = 2 # number of nodes per switch

def mySDNExample(cip="10.1.14.52"):

    net = Mininet(controller=RemoteController, switch=OVSSwitch )

    info( "*** Creating controller, IP: %s\n" % cip)
    c0 = net.addController( name='c0', ip=cip, port=6633 )

    info( "*** Creating switches\n")
    switches = {}
    for s in range(Sw):
        key = "s%s" % s
        sw = net.addSwitch(name=key, cls=OVSSwitch)
        switches.setdefault(key, sw)
        info ("\t*** Created Switch: %s\n" % key)

    info( "*** Creating nodes\n" )
    nodes = {}
    node_counter = 0
    for s in switches.keys():
        nodes.setdefault(s, [])
        for n in range(Nps):
            key = "h%s" % (node_counter)
            node = net.addHost(name=key)
            nodes[s].append(node)
            info ("\t*** Created Node: %s\n" % key)
            node_counter += 1

    info( "*** Creating links\n")
    prev_sw = ""
    first_sw = ""
    for ks,s in switches.items():
        # saving the first switch
        if first_sw is "":
            first_sw = s
        # connecting switches
        if prev_sw is not "":
            net.addLink(s, prev_sw)
        # connecting hosts to corresponding switch
        for h in nodes[ks]:
            net.addLink(s, h)
            info( "\t*** Creating links: %s-%s\n" % (ks,h.name))
        prev_sw = s
    # completing the triangle
    net.addLink(prev_sw, first_sw)

    info( "*** Starting network\n")
    net.build()
    c0.start()
    for k,v in switches.items():
        v.start([ c0 ])

    info( "*** Testing network\n")
    net.pingAll()

    info( "*** Running CLI\n")
    CLI( net )

    info( "*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )  # for CLI output
    Mininet.init()
    mySDNExample()
