import re
import argparse

def get_subdomain_seeds(url):
    # Define a regular expression pattern to extract the subdomain after the first dot and before the third level
    pattern = re.compile(r'\.(\w+(?:-\w+)*\.\w+\.\w+(?:\.\w+){0,1})$')

    # Use the pattern to find matches in the URL
    match = pattern.search(url)

    # Check if a match is found and return the subdomain after the first dot and before the third level
    if match:
        return match.group(1)
    else:
        return None

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-l", "--list", help="file containing subdomains", required=True)
    argparser.add_argument("-o", "--output", help="save output")
    args = argparser.parse_args()

    list_items = set()

    with open(args.list, 'r') as file:
        lines = file.readlines()

    for line in lines:
        subdomain = line.strip()
        subdomain_list = get_subdomain_seeds(subdomain)    
        if subdomain_list:
            list_items.add(subdomain_list)

    with open(args.output, 'w') as output:
        for subdomain_seed in list_items:
            if subdomain_seed is not None:
                output.write(subdomain_seed + '\n')
                print(subdomain_seed)

if __name__=="__main__":
    main()
