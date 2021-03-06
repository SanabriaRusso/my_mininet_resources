#!/usr/bin/python

"""
This example builds a very simple Linear topology using mid-level APIs.
The network is subject to an external SDN Controller.

When we say "external" we mean that the Controller is located outside Mininet's domain.

NOTE: This is a very simple example that only considers 1 switch in the network.
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

Sw = 1 # number of switches
Nps = 2 # number of nodes per switch

def mySDNExample():

    net = Mininet( controller=Controller, switch=OVSSwitch )

    info( "*** Creating controller\n" )
    c0 = net.addController( name='c0', port=6633 )

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

    info( "*** Creating links between host a Switch\n")
    for ks,s in switches.items():
        for h in nodes[ks]:
            net.addLink(s, h)
            info( "\t*** Creating links: %s-%s\n" % (ks,h.name))

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
