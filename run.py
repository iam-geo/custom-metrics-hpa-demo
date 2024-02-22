import argparse

from apps.producer import producer
from apps.consumer import consumer

def main():
    parser = argparse.ArgumentParser(description='Run a module')
    parser.add_argument('module', help='Name module to run')

    args = parser.parse_args()

    module_map = {
        "producer": producer,
        "consumer": consumer
    }

    module_map[args.module]()


if __name__ == "__main__":
    main()