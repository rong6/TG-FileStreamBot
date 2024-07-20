<hr>
<h1 align="center">Telegram File Stream Bot</h1>
<p align="center">
  <a href="https://github.com/EverythingSuckz/TG-FileStreamBot">
    <img src="https://socialify.git.ci/rong6/TG-FileStreamBot/image?font=Source%20Code%20Pro&logo=https://telegra.ph/file/01385a9f4cf0419682b87.png&pattern=Circuit%20Board&theme=Dark" alt="Cover Image" width="650">
  </a>
  <p align="center">
    一个生成Telegram内<b>文件直链</b>的机器人。
  </p>
</p>

<hr>

此仓库源于[EverythingSuckz/TG-FileStreamBot](https://github.com/EverythingSuckz/TG-FileStreamBot)的[python](https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python)分支，遵循[GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.zh-cn.html)。

## 这是啥
这是一个Telegram机器人，它将为您提供 Telegram 文件的流链接，无需等待下载完成。   
目前原仓库使用Go重构的版本有问题，所以我单独把python分支拎出来并构建了Docker镜像。

## 部署
你可以查看原项目的[README](https://github.com/EverythingSuckz/TG-FileStreamBot/blob/python/README.md)以查看详细的部署教程。此处仅提供docker-compose的部署教程。

### docker-compose部署
拉取镜像：
```
docker pull rong6233/tg-filestreambot:latest
```
编辑```docker-compose.yml```文件，参考配置位于仓库根目录下的```docker-compose.yml```内，环境变量具体的配置说明如下：
#### 必选变量
- `API_ID` ：这是您 Telegram 帐户的 API ID，可从 my.telegram.org 获取。 
 
- `API_HASH` ：这是您 Telegram 帐户的 API 哈希，也可以从 my.telegram.org 获取。 
 
- `BOT_TOKEN` ：这是 Telegram Media Streamer Bot 的机器人令牌，可从 [@BotFather](https://telegram.dog/BotFather) 获取。 
 
- `BIN_CHANNEL` ：这是日志频道的频道 ID，机器人将在该频道转发媒体消息并存储这些文件以使生成的直接链接正常工作。要获取频道 ID，请创建一个新的电报频道（公共或私人），在频道中发布一些内容，将消息转发给 [@missrose_bot](https://telegram.dog/MissRose_bot) 并使用 /id 命令 **回复转发的消息**。复制转发的频道 ID 并将其粘贴到此字段中。

#### 可选变量
- `HASH_LENGTH`：这是生成的 URL 的自定义哈希长度。哈希长度必须大于 5 且小于 64。

- `SLEEP_THRESHOLD`：这设置了在机器人实例中全局发生的洪水等待异常的睡眠阈值。引发低于此阈值的洪水等待异常的请求将在睡眠所需的时间后自动再次调用。将引发需要更长等待时间的洪水等待异常。默认值为 60 秒。最好将此字段留空。

- `WORKERS`：这设置了处理传入更新的最大并发工作者数量。默认值为 3。

- `PORT`：这设置了您的 webapp 将监听的端口。默认值为 8080。

- `WEB_SERVER_BIND_ADDRESS`：这设置了您的服务器绑定地址。默认值为 0.0.0.0。

- `NO_PORT` ：这可以是 True 或 False。如果设置为 True，则不会显示端口。
> **注意**
> 要使用此设置，您必须将 `PORT` 指向 HTTP 协议的 80 或 HTTPS 协议的 443，以使生成的链接正常工作。

- `FQDN` ：如果存在，则为完全限定域名。默认为 `WEB_SERVER_BIND_ADDRESS`

- `HAS_SSL` ：可以为 True 或 False。如果设置为 True，则生成的链接将采用 HTTPS 格式。

- `KEEP_ALIVE` ：是否要让服务器每 `PING_INTERVAL` 秒 ping 一次自身以避免休眠。在 PaaS 免费层中很有用。默认为 `False`

- `PING_INTERVAL` ：每次您希望服务器 ping 一次的时间（以毫秒为单位），以避免休眠（如果您使用某些 PaaS）。默认为 `1200` 或 20 分钟。

 - `USE_SESSION_FILE` : 使用客户端的会话文件，而不是将 sqlite 数据库存储在内存中。

#### 多客户端支持
`MULTI_TOKEN1`：在此添加您的第一个机器人令牌。 
 
`MULTI_TOKEN2`：在此添加您的第二个机器人令牌。 
 
您还可以添加任意数量的机器人。（尚未测试最大限制） 
`MULTI_TOKEN3`、`MULTI_TOKEN4` 等。 
 
> **警告** 
> 不要忘记将所有这些机器人添加到 `BIN_CHANNEL` 以确保正常运行


启动：
```
docker-compose up -d
```

## 使用
直接发送/转发文件，稍等片刻，机器人将会返回直链。
![](https://go.xiaobai.mom/https://telegra.ph/file/4ed1d0d46dfaf3f7ff39c.png)