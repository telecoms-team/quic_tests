# Proposed Analytics

## Team Members

* Spencer
* Zoe
* Aaron
## What we are doing for
QUICBBR, TCP RENO, TCP Vegas
## Latency Compared to TCP with TLS (Spencer)

## Performance in Degraded Networks (Spencer)

## Congestion Control (Aaron)
After comparing the following code paramters I have seen a difference up to 0.055312 ms due to the amount of congestion that can be seen.

'''
std::string transport_prot = "QuicBbr";
  double error_p = 0.0;
  std::string bandwidth = "2Mbps";
  std::string delay = "0.01ms";
  std::string access_bandwidth = "12Mbps";
  std::string access_delay = "25ms";
  bool tracing = false;
  std::string prefix_file_name = "QuicVariantsComparison";
  double data_mbytes = 0;
  uint32_t mtu_bytes = 3072;
  uint16_t num_flows = 4;
  float duration = 100;
  uint32_t run = 0;
  bool flow_monitor = false;
  bool pcap = false;
  std::string queue_disc_type = "ns3::PfifoFastQueueDisc";
'''

'''
std::string transport_prot = "QuicBbr";
  double error_p = 0.0;
  std::string bandwidth = "2Mbps";
  std::string delay = "0.01ms";
  std::string access_bandwidth = "12Mbps";
  std::string access_delay = "25ms";
  bool tracing = false;
  std::string prefix_file_name = "QuicVariantsComparison";
  double data_mbytes = 0;
  uint32_t mtu_bytes = 1400;
  uint16_t num_flows = 1;
  float duration = 100;
  uint32_t run = 0;
  bool flow_monitor = false;
  bool pcap = false;
  std::string queue_disc_type = "ns3::PfifoFastQueueDisc";
'''

## Reliable Large Data Transfer (1k bytes and larger) (Aaron)

## Compute Overhead (I don't know how to measure this) (Zoe)

## How to Display Data (Zoe)
