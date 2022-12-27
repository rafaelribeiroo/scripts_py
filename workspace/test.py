from libtorrent import session, parse_magnet_uri
from time import sleep, time

session = session(
    {'listen_interfaces': '0.0.0.0:6881,6882,6883,6884,6885,6886,6887,6888'}
)

params = parse_magnet_uri('magnet:?xt=urn:btih:a207363607321d3110efe4f830651cb0432eee15&amp;dn=The.Really.Loud.House.S01E03.WEBRip.x264-ION10&amp;tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.me%3A2800&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2890&amp;tr=udp%3A%2F%2Ftracker.tallpenguin.org%3A15780&amp;tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12740')
params.save_path = '/tmp/'
# ses.add_torrent_async(params)
handle = session.add_torrent(params)
# handle.set_download_limit(2048)

begin = time()

while not handle.status().has_metadata:
    sleep(1)

print('Downloaded Metadata.')

print("Starting", handle.status().name)

while not handle.status().is_seeding:
    s = handle.status()

    # state_str = ['Queued', 'Checking', 'Downloading Metadata', 'Downloading',
    # 'Finished', 'Seeding', 'Allocating', 'Checking Fastresume']

    # %s: state_str[s.state]
    print(
        f'{s.progress * 100:.2f}% complete'
        f' | Down: {s.download_rate / 1000000:.1f} mb/s'
        f' | Up: {s.upload_rate / 1000000:.1f} mb/s'
        f' | Peers: {s.num_peers}',
        flush=True
    )
    sleep(5)
end = time()
print(handle.status().name, "Complete")
print('Elasped Time:', int((end - begin) // 60), 'min')
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)


from pdb import set_trace; set_trace()
print('continue')
