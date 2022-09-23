#!/usr/bin/python
# 创建网络拓扑
"""Custom topology example
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections


class MyTopo(Topo):
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)
        L1 = 2
        L2 = L1 * 2
        L3 = L2 * 2
        c = []
        a = []
        e = []

        # add computer
        # c0 = net.addController(name='c0',
        #                        controller=Controller,
        #                        protocol='tcp',
        #                        port=6633)
        # add core ovs		核心交换机	Level1		c
        for i in range(L1):
            sw = self.addSwitch('s{}'.format(i + 1))
            c.append(sw)

        # add aggregation ovs	聚合交换机	Level2		a
        for i in range(L2):
            sw = self.addSwitch('s{}'.format(L1 + i + 1))
            a.append(sw)

        # add edge ovs		边缘交换机	Level3		e
        for i in range(L3):
            sw = self.addSwitch('s{}'.format(L1 + L2 + i + 1))
            e.append(sw)

        # add links between computer and ovs
        # for i in range(L1):
        #     sw1 = c[i]
        #     self.addLink(c0, sw1)
        # for i in range(L2):
        #     sw1 = a[i]
        #     self.addLink(c0, sw1)
        # for i in range(L3):
        #     sw1 = e[i]
        #     self.addLink(c0, sw1)

            # add links between core(L1) and aggregation ovs(L2)
        for i in range(L1):
            sw1 = c[i]
            for sw2 in a[0:]:
                # self.addLink(sw2, sw1, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                self.addLink(sw2, sw1)

        # add links between aggregation(L2) and edge ovs(L3)
        for i in range(L2):
            sw1 = a[i]
            j = i // 2
            for sw2 in e[j * 4:j * 4 + 4]:
                self.addLink(sw2, sw1)

	    # add hosts and its links with edge ovs
        count = 1
        for sw1 in e[0:]:
            for i in range(2):
                host = self.addHost('h{}'.format(count))
                self.addLink(sw1, host)
                count += 1


topos = { 'mytopo': (lambda: MyTopo() ) }










