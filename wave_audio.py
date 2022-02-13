import wave

# オーディオデータ内容を見る
def info(audio):
    print(f'サンプリングレートは{audio.getframerate()}Hz')
    print(f'ビット深度は{audio.getsampwidth() * 8}ビット')
    print(f'チャンネル数は{audio.getnchannels()}ch')
    print(f'サンプリング数は{audio.getnframes()}')
    print(f'{audio.getnframes() / audio.getframerate()}秒分のデータ')
    
# オーディオデータを書き出す
def write(channel, bytedepth, framerate, framedata, file_name):
    w = wave.Wave_write(file_name)
    w.setnchannels(channel)
    w.setsampwidth(bytedepth)
    w.setframerate(framerate)
    w.writeframes(framedata)
    w.close()