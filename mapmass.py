import argparse
import subprocess
import os

# Define argument parser
parser = argparse.ArgumentParser(description='Run Masscan and Nmap scans against CIDR, IP, or domain targets.')
parser.add_argument('target', metavar='target', type=str, help='the target(s) to scan, separated by commas')
parser.add_argument('--masscan-args', dest='masscan_args', metavar='args', type=str, default='-p1-65535', help='additional arguments to pass to Masscan (default: -p1-65535)')
parser.add_argument('--nmap-args', dest='nmap_args', metavar='args', type=str, default='-sV', help='additional arguments to pass to Nmap (default: -sV)')
parser.add_argument('--output-dir', dest='output_dir', metavar='dir', type=str, default='results', help='directory to save scan results (default: results)')

args = parser.parse_args()

# Create output directory
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# Split targets string into list
targets = args.target.split(',')

# Run Masscan scans
for target in targets:
    target_out = str(target).replace('/', '_')
    masscan_cmd = f'masscan {target} {args.masscan_args} --rate=10000 -oG {args.output_dir}/{target_out}.gnmap'
    subprocess.run(masscan_cmd, shell=True)
    print(f'Masscan scan for {target} complete.')

# # Run Nmap scans on open ports
# for target in targets:
#     target_out = str(target).replace('/', '_')
#     open_ports = []
#     with open(f'{args.output_dir}/{target_out}.gnmap') as f:
#         for line in f:
#             if 'Ports:' in line:
#                 ports_str = line.strip().split(':')[1]
#                 ports_list = ports_str.split(',')
#                 for port in ports_list:
#                     port_num = port.split('/')[0]
#                     open_ports.append(port_num)
    
#     open_ports_str = ','.join(open_ports)
    
#     nmap_cmd = f'nmap -p{open_ports_str} {args.nmap_args} {target} -oA {args.output_dir}/{target_out}_nmap'
#     subprocess.run(nmap_cmd, shell=True)
#     print(f'Nmap scan for {target} complete.')
