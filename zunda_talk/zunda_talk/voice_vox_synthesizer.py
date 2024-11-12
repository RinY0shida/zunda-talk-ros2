import requests
import json
import os
import tempfile
from playsound import playsound

class VoiceVoxSynthesizer:
    """
    VOICEVOXを使って音声合成と再生を行うクラス
    """
    def __init__(self, base_url="http://localhost:50021"):
        self.base_url = base_url

    def synthesize_and_play(self, text, speaker_id=1):
        """
        入力されたテキストを指定した話者IDの音声で読み上げる関数
        :param text: 読み上げたい文字列
        :param speaker_id: 音声の話者ID（デフォルトは1）
        """
        query_payload = {"text": text, "speaker": speaker_id}
        query_response = requests.post(f"{self.base_url}/audio_query", params=query_payload)

        if query_response.status_code == 200:
            query = query_response.json()

            synthesis_response = requests.post(
                f"{self.base_url}/synthesis",
                params={"speaker": speaker_id},
                json=query
            )

            if synthesis_response.status_code == 200:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                    temp_audio_file.write(synthesis_response.content)
                    audio_filename = temp_audio_file.name
                
                playsound(audio_filename)

                os.remove(audio_filename)

            else:
                print(f"音声合成に失敗: {synthesis_response.status_code}")
        else:
            print(f"クエリの作成に失敗: {query_response.status_code}")
