# pairwise-video-rotate-mirror

## 领域

游戏、图形与多媒体

## 主题

视频旋转镜像元数据

## 说明

元数据归一、镜像裁剪顺序与缩略图方向。

初始状态下 `media/video_rotate_mirror.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
