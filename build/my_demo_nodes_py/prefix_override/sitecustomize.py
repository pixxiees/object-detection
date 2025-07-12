import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pixxelee/Code/SAFMC/penugasan/install/my_demo_nodes_py'
