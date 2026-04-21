import threading
from core.streamer import run_ffmpeg

def stream_to_all(video, platforms, cta):
    threads = []

    for p in platforms:
        t = threading.Thread(
            target=run_ffmpeg,
            args=(video, p["rtmp"], cta)
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
