# -*- coding: utf-8 -*-
"""
Assignment 4.6

Process the ospf_route string and output information to the standard output in the format:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

To do this, use the template pattern and substitute values from the ospf_route string into it.
Values from the ospf_route string should be obtained using Python.

Limitation: All tasks must be performed using only the topics covered.

Warning: In section 4, tests can easily be "cheated" by making the required output,
without obtaining results from the source data using Python.
This does not mean that the task is done correctly, it's just difficult to verify the result at this stage.
"""

route_data = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
"""

route_data = route_data.replace(',', '').replace('via', '').split()
print(template.format(route_data[0], route_data[1],
      route_data[2], route_data[3], route_data[4]))
