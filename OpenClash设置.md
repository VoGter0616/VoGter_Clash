
# OpenClash 使用设置

> 本文档面向 OpenWrt / iStoreOS / ImmortalWrt 上的 OpenClash，涵盖覆写模块、模式设置、DNS、GEO 数据库、覆写设置、规则设置与订阅配置。
> 首次使用建议按“首页 → 插件设置 → 覆写设置 → 规则设置 → 配置订阅”的顺序阅读。

> [!TIP]
> 以下所有可复制粘贴的内容（除覆写模块和自定义规则外）均直接复制覆盖到配置里即可。

---

## 一、首页

### 1.1 运行状态 —— 覆写模块（OpenClash v0.47.081 以上版本）

> [!TIP]
> 在 `openclash_custom_overwrite.sh` 文件内的 `exit 0` 上方、`CONFIG_FILE="$1"` 的下方粘贴并修改成所需机场节点域名解析 DNS（用来解析AnyTLS协议节点）。没有或者不知道专属 DNS，无视此条设置。

    ruby_edit "$CONFIG_FILE" "['dns']['proxy-server-nameserver']" "[' DoH1',' DoH2']"

### 1.2 示例

    openclash_custom_overwrite.sh
    CONFIG_FILE="$1"

    ruby_edit "$CONFIG_FILE" "['dns']['proxy-server-nameserver']" "['https://abc.xxx.com/dns1_query','https://abc.xxx.com/dns2_query']"
    exit 0

---

---

## 二、插件设置

### 2.1 模式设置

- 运行模式：**Fake-ip（TUN-混合）模式**
- 网络栈类型：**System**
- 代理模式：**Rule（策略代理）**
- 旁路网关（旁路由）兼容 ✅（如果是旁路由勾选）
- 其他默认

### 2.2 流量控制

- 路由本机代理 ✅
- 禁用 QUIC ✅
- 绕过服务器地址 ✅
- 实验性：绕过指定区域 IP：**绕过中国大陆**
- 其他默认

**绕过指定区域 IPv4 黑名单里覆盖添加：**

    services.googleapis.cn
    googleapis.cn
    xn--ngstr-lra8j.com
    adobe.com
    adobelogin.com
    adobe.io
    behance.net

### 2.3 DNS 设置

- 本地 DNS 劫持：**使用 Dnsmasq 转发**
- 其他默认

### 2.4 流媒体增强

如果有详细的分流规则，则不用设置（默认不设置）。

### 2.5 黑白名单

默认不设置。

### 2.6 外部控制

默认不设置。

### 2.7 IPv6 设置

**默认关闭。** 如果使用按照以下设置，且必须保证节点支持 IPv6 和路由 IPv6 的设置正确。如果节点不支持 IPv6 还需要使用，设置好路由的 IPv6 后开启“允许 IPv6 类型 DNS 解析”。

- IPv6 流量代理 ✅
- IPv6 代理模式：**Mix 混合模式**
- 允许 IPv6 类型 DNS 解析 ✅
- Fake-IP 地址范围（IPv6 Cidr）：`fdfe:dcba:9876::1/64`
- 实验性：绕过指定区域 IPv6：**绕过中国大陆**
- 其他默认

### 2.8 GEO 数据库订阅

- 自动更新 GeoIP MMDB 数据库 ✅

      https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/country.mmdb

- 自动更新 GeoIP Dat 数据库 ✅

      https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat

- 自动更新 GeoSite 数据库 ✅

      https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat

### 2.9 大陆白名单订阅

开启自动更新，全部默认即可。

### 2.10 定时重启

默认设置（根据自身情况设置）。

### 2.11 版本更新

根据设备选择编译版本。

- 更新分支：**Master**
- 使用 Smart 内核就开启 Smart 内核更新，不使用就默认停用

### 2.12 开发者选项

默认不设置。

### 2.13 内核测试

默认不设置。

### 2.14 oicCloud

默认不设置。

---

## 三、覆写设置

### 3.1 常规设置

- Github 地址修改：`https://testingcf.jsdelivr.net/`（代理通后将此选项改为**禁用**）
- 其他默认

### 3.2 DNS 设置

- 自定义上游 DNS 服务器 ✅
- 遵循规则（respect-rules）✅
- Fake-IP 持久化 ✅
- Fallback-Filter ✅

**Fallback-Filter 配置（覆盖原有配置）：**

    fallback-filter:
      geoip: true
      geoip-code: CN
      ipcidr:
        - 10.0.0.0/8
        - 100.64.0.0/10
        - 127.0.0.0/8
        - 169.254.0.0/16
        - 172.16.0.0/12
        - 192.168.0.0/16
        - 224.0.0.0/4
      domain:
        # =========================================================
        # Google / Gemini / YouTube
        # =========================================================
        - "+.google.com"
        - "+.googleapis.com"
        - "+.gstatic.com"
        - "+.googleusercontent.com"
        - "+.googlevideo.com"
        - "+.googleadservices.com"
        - "+.googlesyndication.com"
        - "+.doubleclick.net"
        - "+.ggpht.com"
        - "+.youtube.com"
        - "+.youtube-nocookie.com"
        - "+.ytimg.com"
        - "+.youtu.be"
        - "+.gemini.google.com"
        - "+.ai.google.dev"
        - "+.generativelanguage.googleapis.com"
        - "+.aistudio.google.com"

        # =========================================================
        # OpenAI / ChatGPT
        # =========================================================
        - "+.openai.com"
        - "+.chatgpt.com"
        - "+.oaistatic.com"
        - "+.oaiusercontent.com"
        - "+.oaistatsig.com"

        # OpenAI 依赖的部分第三方服务
        - "+.challenges.cloudflare.com"
        - "+.workos.com"
        - "+.workos.imgix.net"
        - "+.workoscdn.com"
        - "+.intercom.io"
        - "+.intercomcdn.com"
        - "+.sentry.io"
        - "+.datadoghq.com"

        # =========================================================
        # Anthropic / Claude
        # =========================================================
        - "+.anthropic.com"
        - "+.claude.ai"
        - "+.claude.com"

        # =========================================================
        # AI / 开发者 AI 服务
        # =========================================================
        - "+.huggingface.co"
        - "+.hf.co"
        - "+.replicate.com"
        - "+.perplexity.ai"
        - "+.poe.com"
        - "+.cohere.com"
        - "+.mistral.ai"
        - "+.mistral.com"
        - "+.groq.com"
        - "+.x.ai"
        - "+.grok.com"
        - "+.cursor.com"
        - "+.cursor.sh"
        - "+.windsurf.com"
        - "+.codeium.com"

        # =========================================================
        # GitHub / GitLab / 开发者服务
        # =========================================================
        - "+.github.com"
        - "+.githubusercontent.com"
        - "+.githubassets.com"
        - "+.github.io"
        - "+.gitlab.com"
        - "+.gitlab.io"
        - "+.bitbucket.org"
        - "+.sourcegraph.com"
        - "+.npmjs.com"
        - "+.npmjs.org"
        - "+.pypi.org"
        - "+.pythonhosted.org"
        - "+.docker.com"
        - "+.docker.io"
        - "+.dockerusercontent.com"
        - "+.jsdelivr.net"
        - "+.unpkg.com"
        - "+.cdnjs.com"
        - "+.cdnjs.cloudflare.com"

        # =========================================================
        # Cloudflare / CDN / DNS
        # =========================================================
        - "+.cloudflare.com"
        - "+.cloudflare-dns.com"
        - "+.cloudflareclient.com"
        - "+.workers.dev"
        - "+.pages.dev"
        - "+.cloudfront.net"
        - "+.fastly.net"
        - "+.akamaized.net"
        - "+.akamaihd.net"
        - "+.edgekey.net"
        - "+.edgesuite.net"

        # =========================================================
        # Facebook / Instagram / Meta
        # =========================================================
        - "+.facebook.com"
        - "+.facebook.net"
        - "+.fbcdn.net"
        - "+.fbsbx.com"
        - "+.instagram.com"
        - "+.cdninstagram.com"
        - "+.threads.net"
        - "+.threads.com"
        - "+.whatsapp.com"
        - "+.whatsapp.net"

        # =========================================================
        # X / Twitter
        # =========================================================
        - "+.x.com"
        - "+.twitter.com"
        - "+.twimg.com"

        # =========================================================
        # Telegram
        # =========================================================
        - "+.telegram.org"
        - "+.t.me"
        - "+.telegra.ph"
        - "+.telegram.me"
        - "+.telegram.dog"

        # =========================================================
        # Reddit
        # =========================================================
        - "+.reddit.com"
        - "+.redditmedia.com"
        - "+.redditstatic.com"
        - "+.redd.it"

        # =========================================================
        # Discord
        # =========================================================
        - "+.discord.com"
        - "+.discordapp.com"
        - "+.discordapp.net"
        - "+.discord.gg"
        - "+.discord.media"

        # =========================================================
        # Microsoft / Azure / Copilot
        # =========================================================
        - "+.microsoft.com"
        - "+.microsoftonline.com"
        - "+.msauth.net"
        - "+.msftauth.net"
        - "+.live.com"
        - "+.office.com"
        - "+.office.net"
        - "+.office365.com"
        - "+.azure.com"
        - "+.azureedge.net"
        - "+.windows.net"
        - "+.bing.com"
        - "+.bingapis.com"
        - "+.copilot.microsoft.com"

        # =========================================================
        # Apple
        # =========================================================
        - "+.apple.com"
        - "+.icloud.com"
        - "+.icloud-content.com"
        - "+.mzstatic.com"
        - "+.itunes.apple.com"
        - "+.push.apple.com"

        # =========================================================
        # Amazon / AWS
        # =========================================================
        - "+.amazon.com"
        - "+.amazonaws.com"
        - "+.amazonvideo.com"
        - "+.aws.amazon.com"

        # =========================================================
        # Netflix
        # =========================================================
        - "+.netflix.com"
        - "+.netflix.net"
        - "+.nflxvideo.net"
        - "+.nflximg.net"
        - "+.nflximg.com"
        - "+.nflxso.net"
        - "+.nflxext.com"

        # =========================================================
        # Spotify
        # =========================================================
        - "+.spotify.com"
        - "+.spotifycdn.com"
        - "+.scdn.co"

        # =========================================================
        # Disney+
        # =========================================================
        - "+.disneyplus.com"
        - "+.disney-plus.net"
        - "+.dssott.com"
        - "+.media.dssott.com"

        # =========================================================
        # Twitch
        # =========================================================
        - "+.twitch.tv"
        - "+.twitchcdn.net"
        - "+.ttvnw.net"

        # =========================================================
        # 游戏 / Steam / Epic / PlayStation / Xbox
        # =========================================================
        - "+.steampowered.com"
        - "+.steamcommunity.com"
        - "+.steamstatic.com"
        - "+.steamcontent.com"
        - "+.steamusercontent.com"
        - "+.steamserver.net"
        - "+.epicgames.com"
        - "+.epicgamescdn.com"
        - "+.playstation.com"
        - "+.playstation.net"
        - "+.xbox.com"
        - "+.xboxlive.com"
        - "+.ea.com"
        - "+.eaassets.com"
        - "+.ubisoft.com"
        - "+.ubisoftconnect.com"
        - "+.rockstargames.com"
        - "+.nvidia.com"

        # =========================================================
        # 常用国外资讯 / 社区
        # =========================================================
        - "+.wikipedia.org"
        - "+.wikimedia.org"
        - "+.medium.com"
        - "+.quora.com"
        - "+.stackexchange.com"
        - "+.stackoverflow.com"
        - "+.stackprinter.com"

        # =========================================================
        # 隐私 / DNS / 网络测试
        # =========================================================
        - "+.browserleaks.com"
        - "+.dnsleaktest.com"
        - "+.ipleak.net"
        - "+.ipinfo.io"
        - "+.whatismyipaddress.com"
        - "+.whatismyip.com"
        - "+.whoer.net"

        # =========================================================
        # NTP / 时间同步
        # =========================================================
        - "+.pool.ntp.org"
        - "+.ntp.org"

        # =========================================================
        # 补充：常用协作 / 工具服务
        # =========================================================
        - "+.notion.so"
        - "+.figma.com"
        - "+.slack.com"
        - "+.zoom.us"
        - "+.teamviewer.com"
        - "+.services.mozilla.com"

- Fake-IP-Filter ✅
- Fake-IP-Filter-Mode：**黑名单模式**

**Fake-IP-Filter 配置（覆盖原有配置）：**

    *.somethingstranges.com
    *.lan
    *.localdomain
    *.example
    *.invalid
    *.localhost
    *.test
    *.local
    *.home.arpa
    *.direct
    cable.auth.com
    network-test.debian.org
    detectportal.firefox.com
    resolver1.opendns.com
    global.turn.twilio.com
    global.stun.twilio.com
    app.yinxiang.com
    injections.adguard.org
    +.weixin.qq.com
    *.blzstatic.cn
    *.cmpassport.com
    id6.me
    open.e.189.cn
    opencloud.wostore.cn
    id.mail.wo.cn
    mdn.open.wo.cn
    hmrz.wo.cn
    nishub1.10010.com
    enrichgw.10010.com
    *.wosms.cn
    *.jegotrip.com.cn
    *.icitymobile.mobi
    *.pingan.com.cn
    *.cmbchina.com
    *.10099.com.cn
    *.microdone.cn
    +.msftconnecttest.com
    +.msftncsi.com
    *.time.edu.cn
    *.ntp.org.cn
    time.android.com
    time.windows.com
    +.pool.ntp.org
    music.163.com
    *.music.163.com
    *.126.net
    musicapi.taihe.com
    music.taihe.com
    songsearch.kugou.com
    trackercdn.kugou.com
    *.kuwo.cn
    api-jooxtt.sanook.com
    api.joox.com
    joox.com
    y.qq.com
    *.y.qq.com
    streamoc.music.tc.qq.com
    mobileoc.music.tc.qq.com
    isure.stream.qqmusic.qq.com
    dl.stream.qqmusic.qq.com
    aqqmusic.tc.qq.com
    amobile.music.tc.qq.com
    *.xiami.com
    *.music.migu.cn
    music.migu.cn
    localhost.ptlogin2.qq.com
    localhost.sec.qq.com
    +.qq.com
    +.tencent.com
    +.wechat.com
    +.servicewechat.com
    +.qqmail.com
    +.gtimg.com
    +.qpic.cn
    +.qlogo.cn
    +.tenpay.com
    +.myqcloud.com
    +.qcloud.com
    +.qcloudcdn.com
    +.dnsv1.com
    +.taobao.com
    +.tmall.com
    +.alicdn.com
    +.alibaba.com
    +.alibabausercontent.com
    +.alipay.com
    +.alipayobjects.com
    +.goofish.com
    +.idlefish.com
    +.aliyun.com
    +.aliyuncs.com
    +.mmstat.com
    +.cainiao.com
    +.amap.com
    +.autonavi.com
    +.fhnfile.oss-cn-shenzhen.aliyuncs.com
    +.kunlunca.com
    +.kunlungr.com
    +.aliclouddns.com
    +.baidu.com
    +.shifen.com
    +.bdstatic.com
    +.bdydns.com
    +.baidubce.com
    +.bcebos.com
    +.douyin.com
    +.douyincdn.com
    +.douyinpic.com
    +.douyinstatic.com
    +.douyinliving.com
    +.iesdouyin.com
    +.douyinvod.com
    +.douyinvideo.net
    +.amemv.com
    +.snssdk.com
    +.byteimg.com
    +.ibytedtos.com
    +.zijieapi.com
    +.pstatp.com
    +.toutiao.com
    +.toutiaovod.com
    +.bytedance.net
    +.jd.com
    +.jcloudimg.com
    +.jd360.hk
    +.360buyimg.com
    +.jcloud.com
    +.bilibili.com
    +.bilicdn1.com
    +.hdslb.com
    +.163.com
    +.126.com
    +.netease.com
    +.163jiasu.com
    +.iqiyi.com
    +.qy.net
    +.iqiyipic.com
    +.youku.com
    +.ykimg.com
    +.tudou.com
    +.xiaohongshu.com
    +.xhscdn.com
    +.xhscdn.net
    +.xhslink.com
    +.xhsimg.com
    +.pinduoduo.com
    +.pinduoduo.net
    +.yangkeduo.com
    +.kuaishou.com
    +.yximgs.com
    +.ksapisrv.com
    +.meituan.com
    +.meituan.net
    +.dianping.com
    +.dpfile.com
    +.zhihu.com
    +.zhimg.com
    +.sina.com.cn
    +.weibo.com
    dlg.io.mi.com
    +.115.com
    +.115cdn.com
    +.115cdn.net
    +.115img.com
    +.116cd.com
    +.116cd.net
    +.anxia.com
    +.sq.cc
    +.xunlei.com
    +.sandai.net
    +.n0808.com
    +.wscdns.com
    +.chinanetcenter.com
    +.ourglu.com
    +.qingcdn.com
    +.qiniu.com
    +.qiniucdn.com
    +.clouddn.com
    +.ksyun.com
    +.ksyuncs.com
    +.360tpcdn.com
    +.mi.com
    +.xiaomi.com
    +.market.xiaomi.com
    +.miui.com
    +.huawei.com
    +.vmall.com
    +.csdn.net
    +.jianshu.com
    +.sohu.com
    +.sogou.com
    +.cn
    +.battlenet.com.cn
    +.wotgame.cn
    +.wggames.cn
    +.wowsgame.cn
    mesu.apple.com
    swscan.apple.com
    swquery.apple.com
    swdownload.apple.com
    swcdn.apple.com
    swdist.apple.com
    lens.l.google.com
    stun.l.google.com
    na.b.g-tun.com
    +.stun.playstation.net
    heartbeat.belkin.com
    *.linksys.com
    *.linksyssmartwifi.com
    *.router.asus.com
    local.adguard.org
    +.pub.3gppnetwork.org
    +.uu.163.com
    ps.res.netease.com
    +.media.dssott.com
    shark007.net
    +.wilds.monsterhunter.com
    +.playfabapi.com
    +.cloudapp.azure.com
    +.westeurope.cloudapp.azure.com
    +.vodafone-ip.de
    mask.icloud.com
    mask-h2.icloud.com
    mask.apple-dns.net
    # DDNS/内网穿透（请替换为你的实际DDNS域名）
    # +.ddnsddns.com
    # +.tailscale.com
    live-push.bilivideo.com

**设置自定义上游 DNS 服务器**（在上方设置中启用本功能后生效）：

| 服务器分组 | 服务器地址 | 服务器类型 | 状态 | 操作 |
| --- | --- | --- | --- | --- |
| nameserver | 223.5.5.5 | UDP | 启用 | |
| nameserver | 119.29.29.29 | UDP | 启用 | |
| nameserver | dhcp://system | UDP | 启用 | 旁路由模式下将其改成主路由网关，默认关闭 |
| fallback | 1.1.1.1/dns-query#PROXY | HTTPS | 启用 | PROXY 为策略节点组配置里的策略组 |
| fallback | dns.google/dns-query#PROXY | HTTPS | 启用 | PROXY 为策略节点组配置里的策略组 |
| default-nameserver | 223.5.5.5 | UDP | 启用 | |
| default-nameserver | 119.29.29.29 | UDP | 启用 | |
| default-nameserver | 2400:3200::1 | UDP | 启用 | 使用 IPv6 DNS 解析时开启 |

### 3.3 Meta 设置

- 启用 TCP 并发 ✅
- 启用统一延迟 ✅
- 其他默认
- 启用流量（域名）探测 ✅
- 探测（嗅探）纯 IP 连接 ✅
- 自定义流量探测（嗅探）设置 ✅

**嗅探配置（覆盖原有配置）：**

    # 嗅探域名 可选配置
    sniffer:
      force-dns-mapping: true
      parse-pure-ip: true
      override-destination: true
      sniff:
        QUIC:
          ports: [443]
        TLS:
          ports: [443, 8443]
        HTTP:
          ports: [80, 8080-8880]
          override-destination: true
      force-domain:
        - "+.netflix.com"
        - "+.nflxvideo.net"
        - "+.amazonaws.com"
        - "+.media.dssott.com"
        - "+.google.com"
        - "+.googleapis.com"
        - "+.youtube.com"
        - "+.googlevideo.com"
        - "+.facebook.com"
        - "+.instagram.com"
        - "+.twitter.com"
        - "+.telegram.org"
        - "+.openai.com"
        - "+.chatgpt.com"
      skip-domain:
        # 腾讯/微信系
        - "+.qq.com"
        - "+.tencent.com"
        - "+.wechat.com"
        - "+.gtimg.com"
        - "+.qpic.cn"
        - "+.qlogo.cn"
        - "+.myqcloud.com"
        - "+.qcloud.com"
        # 字节跳动/抖音系
        - "+.douyin.com"
        - "+.douyincdn.com"
        - "+.douyinpic.com"
        - "+.iesdouyin.com"
        - "+.douyinvod.com"
        - "+.amemv.com"
        - "+.snssdk.com"
        - "+.byteimg.com"
        - "+.ibytedtos.com"
        - "+.toutiao.com"
        - "+.bytedance.net"
        # 小红书
        - "+.xiaohongshu.com"
        - "+.xhscdn.com"
        - "+.xhslink.com"
        # 阿里系
        - "+.taobao.com"
        - "+.tmall.com"
        - "+.alicdn.com"
        - "+.alibaba.com"
        - "+.alipay.com"
        - "+.aliyun.com"
        - "+.aliyuncs.com"
        - "+.amap.com"
        # 115网盘
        - "+.115.com"
        - "+.115cdn.com"
        - "+.115img.com"
        - "+.116cd.com"
        - "+.anxia.com"
        - "+.sq.cc"
        # 小米
        - "+.mi.com"
        - "+.dlg.io.mi.com"
        # 苹果推送
        - "+.push.apple.com"
        # 国内大厂CDN
        - "+.baidu.com"
        - "+.bdstatic.com"
        - "+.jd.com"
        - "+.bilibili.com"
        - "+.163.com"
        - "+.youku.com"
        - "+.meituan.com"
        - "+.zhihu.com"
        - "+.weibo.com"
        - "+.sina.com.cn"
      # skip-src-address:
      #   - 192.168.0.3/32
      # skip-dst-address:
      #   - 192.168.0.3/32

### 3.4 Smart 设置

根据个人使用情况设置。

---

## 四、规则设置

- 仅代理命中规则流量 ✅
- 自定义规则 ✅

> [!WARNING]
> 在（优先匹配）的 `rules:` 下行填写以下内容。

    # 1. NTP 端口强制直连（最高优先级）
    - DST-PORT,123,DIRECT

    # 2. 禁用阿里系 UDP 443 端口 (HTTP/3 / QUIC)
    - AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,alibaba)),REJECT

    # 3. 禁用腾讯系 UDP 443 端口
    - AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,tencent)),REJECT

    # 4. 禁用字节跳动系 UDP 443 端口
    - AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,bytedance)),REJECT

    # 5. 其他自定义规则...
    #- DOMAIN,局域网内DDNS域名,DIRECT

---

## 五、配置订阅

| 配置项 | 值 |
| --- | --- |
| 配置文件名 | （自定义） |
| 订阅地址 | （自定义） |
| User-Agent | `clash.meta/1.19.20` |
| 在线订阅转换 | ✅ |
| 订阅转换服务地址 | 自己的后端（版本 0.9.9）或者 `api.asailor.org` 尝试转换 |
| 订阅转换模板 | 自定义模板 |
| 自定义模板地址 | `https://cdn.jsdelivr.net/gh/VoGter0616/VoGter_Clash@main/cfg/Clash_custom.ini` |
| 跳过证书验证 | 启用 |

其他参数根据自身情况设置。

---

## 六、推荐阅读顺序

1. **首页**：确认覆写模块是否需要修改节点域名解析 DNS。
2. **插件设置**：模式设置 → 流量控制 → DNS 设置 → GEO 数据库订阅。
3. **覆写设置**：常规设置 → DNS 设置 → Meta 设置 → Smart 设置。
4. **规则设置**：按需启用“仅代理命中规则流量”，填写自定义规则。
5. **配置订阅**：填写订阅地址、User-Agent、订阅转换模板与模板地址。
