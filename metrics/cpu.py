from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server, Info
from jtop import jtop


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
        while jetson.ok():
        # Read tegra stats
            print(jetson.cpu)