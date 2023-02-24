# MapMass
This Python script can be used to run Masscan and Nmap scans against CIDR, IP, or domain targets, and save the results in separate folders. The script accepts user-defined parameters for Masscan and Nmap commands, such as port range, scan rate, and additional options.

## Requirements
To use this script, you'll need to have the following software installed:

* Python 3.x (tested with Python 3.9.5)
* Masscan (tested with Masscan 1.3.4)
* Nmap (tested with Nmap 7.91)
> Note: Masscan and Nmap must be available in your system's PATH.

## Installation
* Clone or download the massmap.py file to your local machine.
* Open a terminal or command prompt and navigate to the directory where the massmap.py file is saved.
* Run the following command to download and run the dependency installation script:
  ` bash <(curl -s https://raw.githubusercontent.com/m4rvxpn/masscan-nmap-scanner/main/dependencies.sh) `
  Replace username with the appropriate username for the GitHub repository containing the dependency installation script.
* Wait for the script to complete. The script installs Python 3.x, Masscan, and Nmap on your system.
* You can now use the massmap.py script to scan targets with Masscan and Nmap as needed. See the README file for usage instructions and customization options.
> Note: These installation steps assume you're running a Debian-based Linux distribution (such as Ubuntu) and have administrative privileges. If you're running a different operating system, you may need to adjust the commands accordingly.

## Usage
* Clone or download the massmap.py file to your local machine.
* Open a terminal or command prompt and navigate to the directory where the massmap.py file is saved.
* Run the script with the following command:

  ` python massmap.py <target> [--masscan-args <args>] [--nmap-args <args>] [--output-dir <dir>] `
  Replace <target> with the target(s) you want to scan, separated by commas. You can also provide optional arguments to customize Masscan and Nmap commands, such as --masscan-args '-p80,443' to scan only ports 80 and 443 with Masscan, or --nmap-args '-sS -A' to use SYN scan and aggressive service detection with Nmap. By default, Masscan scans all ports (1-65535) and Nmap uses service version detection (-sV). You can also specify an output directory using the --output-dir option, which defaults to results.

* Wait for the script to complete. Masscan scans and Nmap scans on open ports will be saved in separate folders within the specified or default output directory.

## Output
The script saves the following files in the output directory:

* ` <target>.gnmap `: Masscan scan results in GNmap format
* ` <target>_nmap.xml `: Nmap scan results in XML format
* ` <target>_nmap.nmap `: Nmap scan results in Nmap format
If you use the ` -oA ` option with Nmap, the script will also save merged results in three formats (` <target>_nmap.gnmap, <target>_nmap.txt, and <target>_nmap.xml `).

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
Make sure to add the LICENSE file to your repository as well. You can generate a MIT license using websites like Choose a License.

## Contributing
If you find a bug or have a feature request, please create an issue on the GitHub repository. You can also submit a pull request with your proposed changes.
