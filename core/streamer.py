import subprocess
from core.overlay import get_overlay_position

def run_ffmpeg(video, rtmp, cta=None):
    position = get_overlay_position()

    cmd = [
        "ffmpeg",
        "-re",
        "-i", video
    ]

    if cta:
        cmd += [
            "-ignore_loop", "0",
            "-i", cta,
            "-filter_complex",
            f"[0:v][1:v] overlay={position}"
        ]

    cmd += [
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "2500k",
        "-c:a", "aac",
        "-f", "flv",
        rtmp
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd)
