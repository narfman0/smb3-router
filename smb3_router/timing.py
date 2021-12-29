NES_FRAMERATE = 60.0988


def frames_to_duration_string(frames):
    return seconds_to_duration_string(frames_to_seconds(frames))


def frames_to_seconds(frames):
    return frames // NES_FRAMERATE


def seconds_to_duration_string(seconds):
    return f"{int(seconds // 60)}:{'{:02d}'.format(int(seconds % 60))}"