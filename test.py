import pyaudio
import wave


# チャンクサイズ(粒度)
CHUNK_SIZE = 1024
 
# WAVファイルを開く
wf = wave.open('test.wav', 'rb')
 
# PyAudioインスタンスを作成する
p = pyaudio.PyAudio()

for x in range(0, p.get_device_count()):
    print(p.get_device_info_by_index(x)['name'])
 
# Streamを開く。フォーマット・チャンネル・サンプリングレートをWAVファイルと
# 合わせているが、合わせなくても再生は行える。
# ちなみにフォーマットとはビット深度のことであり、
# 8bitなら「p.get_format_from_width(1)」、
# 16bitなら「p.get_format_from_width((2)」とバイト数で設定することに注意
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                input_device_index=3)
 
# データをチャンクサイズだけ読み込む
data = wf.readframes(CHUNK_SIZE)
 
# Streamに読み取ったデータを書き込む＝再生する
while len(data) > 0:
    # Streamに書き込む
    stream.write(data)
 
    # 再度チャンクサイズだけ読み込む。これを繰り返す
    data = wf.readframes(CHUNK_SIZE)
 
# Streamを止めて、closeする。closeしなければ、start_stream()で再開できる
stream.stop_stream()
stream.close()
 
# PyAudioインスタンスを破棄する
p.terminate()