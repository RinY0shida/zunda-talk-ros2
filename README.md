# zunda_talk_ros2
ずんだもんの声でお話してくれるpkg

### 環境
- ros2 humble
- voicevox

### 起動方法
- voicevoxの起動をする
- `colcon build`をする
- `source install/setup.bash`をする
- `ros2 run zunda_talk zunda_talk`をする

### 実際におしゃべりさせる
- `ros2 topic pub -1 /zunda_talk std_msgs/msg/String "{data: huga}"` publishするとおしゃべりしてくれます。

### 利用規約
- https://zunko.jp/con_ongen_kiyaku.html

### Credits
- [VOICEVOX](https://voicevox.hiroshiba.jp/):ずんだもん
