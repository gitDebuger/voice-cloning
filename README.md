# Voice Cloning Learning

这里将尝试学习使用一些常见的声音复刻大模型，目前已有阿里云百炼大模型、字节跳动火山引擎大模型。

当前项目使用UV进行管理，Python版本为3.12.10。

## 1. 火山引擎

字节跳动火山引擎旗下的声音复刻模型名为**Doubao-声音复刻**。

创建音色一般需要使用本地音频文件，并且免费音色每用户只有一个。

## 2. 阿里云百炼

阿里云百炼旗下的声音复刻模型包含**cosyvoice-v1**和**cosyvoice-v2**。

创建音色需要提供音频URL，可使用阿里云OSS服务存储音频文件。每个阿里云主账号最多可同时保留1000个复刻音色。

