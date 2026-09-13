<div align="center">

# 🔧 VoGter 的自用模板库

</div>

</p>

---

## 📂 目录结构

| 目录 / 文件 | 描述 |
| :--- | :--- |
| [/.github](./.github) | 自动化脚本及工具。 |
| [/rule](./rule) | 规则集。 |
| [Clash_IPLC_VIP.ini](./cfg/Clash_IPLC_VIP.ini) | OpenClash 自定义转换文件，机场 IPLC.app 专用。 |
| [Clash_custom.ini](./cfg/Clash_custom.ini) | OpenClash 自定义转换文件。 |
| [Clash_test.ini](./cfg/Clash_test.ini) | OpenClash 转换前测试文件。 |
| [Clash_Verge.ini](./cfg/Clash_Verge.ini) | Clash Verge 自定义转换文件。 |
| [Shadowrocket_basic.conf](./cfg/Shadowrocket_basic.conf) | Shadowrocket 自定义配置文件。 |
| [Surge_basic.conf](./cfg/Surge_basic.conf) | Surge 自定义配置文件。 |

---

<details>
<summary><b>📄 点击展开 / 折叠查看：OpenClash 设置指南</b></summary>

<br>

<!-- OPENCLASH_START -->

# OpenClash 使用设置

> 本文档面向 OpenWrt / iStoreOS / ImmortalWrt 上的 OpenClash，涵盖覆写模块、模式设置、DNS、GEO 数据库、覆写设置、规则设置与订阅配置。
> 首次使用建议按“首页 → 插件设置 → 覆写设置 → 规则设置 → 配置订阅”的顺序阅读。

> [!WARNING]
> Clash订阅转换服务地址的公共后端暂不支持AnyTLS等新协议节点的转换
>
> 如使用自定义规则模板需要转换订阅服务需自行部署asdlokj1qpi23/subconverter后端进行转换使用

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

> [!TIP]
> 默认关闭
> 
> 如果使用按照以下设置，且必须保证节点支持 IPv6 和路由 IPv6 的设置正确。如果节点不支持 IPv6 还需要使用，设置好路由的 IPv6 后仅开启“允许 IPv6 类型 DNS 解析”。

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
| 订阅转换服务地址 | 自己的后端（版本 0.9.9）（注！公用后端暂不支持AnyTLS协议转换，建议自己搭建asdlokj1qpi23/subconverter后端使用） |
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

<!-- OPENCLASH_END -->

</details>

<details>
<summary><b>📄 点击展开 / 折叠查看：Shadowrocket 设置指南</b></summary>

<br>

<!-- SHADOWROCKET_START -->

# Shadowrocket 使用设置

> 本文档面向 iOS / iPadOS / macOS 上的 Shadowrocket，涵盖订阅、配置、证书、DNS、分流与常见问题。
> 首次使用建议按“首页 → 配置 → 设置 → 数据”的顺序阅读。

---

## 一、首页

### 1.1 订阅节点

- 点击右上角 **＋** 号添加节点，类型根据你的机场提供的订阅进行设置（部分机场支持一键导入 Shadowrocket）。
- 其他设置保持默认即可。
- 过滤可以使用正则表达式来过滤不需要的节点。

**过滤正则提示词：**

`^(?!.*(xxxx|xxxx)).*$`

在小火箭的过滤正则中填入，并把 `xxxx` 替换为你需要过滤的节点关键词。

### 1.2 快速使用方法

1. 首页 → 添加节点。
2. 设置 → 延迟测试方法，选择 **CONNECT**。
3. 首页 → 连通性测试，选择可用节点连接。

> 首次启动会提示【安装 VPN 配置文件】，请点击【好】和【允许】才能正常使用。

### 1.3 全局路由：配置

首页 → 全局路由 → 选择 **配置**。

> 全局代理模式（Proxy）下 DNS 通常不走代理，只有配置（Config）模式下才可能正确走代理。如果你更在意 DNS 防泄漏，建议使用配置模式，并正确设置 `dns-server` 的 `#proxy=` 参数。

---

## 二、配置

### 2.1 订阅配置

点击右上角 **＋** 号，从给定的 URL 下载配置。

**配置文件地址：**

`https://raw.githubusercontent.com/VoGter0616/VoGter_Clash/main/cfg/Shadowrocket_basic.conf`

复制粘贴后点击下载，等待下载完成即可。

> Raw 地址需要代理才可以正常访问 GitHub 下载。如果没有代理条件，可以把上述地址转换成国内 CDN 地址，再复制粘贴并下载即可使用。
>
> 提示词：`转换成 testingcf.jsdelivr.net/加速连接`

> [!TIP]
> 如果需要使用特定 DNS 解析域名，在 **配置 → 本地文件** 里选择 `Shadowrocket_basic.conf`，长按选择 **编辑纯文本**，翻阅至最底部的 `[Host]` 进行修改。如果无特殊需求，无视此操作。

### 2.2 使用配置（仅 iPhone 设置，Mac 默认即可）

1. 长按本地文件下载好的 `Shadowrocket_basic.conf`，点击 **使用配置**。
2. 点击 `Shadowrocket_basic.conf` 右侧 **ⓘ** 进入配置文件，依次点击：
   **HTTPS 解密 → 打开 HTTPS 解密 → 证书授权 → 证书 → 生成新的 CA 证书 → 安装证书 → 允许 → 点击右上角的 √ 保存**。
3. 返回桌面，依次点击：
   **设置 → 通用 → VPN 与设备管理 → 已下载的描述文件 → 点击 Shadowrocket 的文件 → 右上角安装 → 输入锁屏密码 → 右上角安装**。
4. 回到 Shadowrocket，点击右上角确认即可正常使用配置文件。

### 2.3 HTTPS 解密方法

1. 点击“配置文件”后面 **ⓘ** → **HTTPS 解密** → **证书** → **生成新的 CA 证书** → **安装证书**。
2. **系统设置 → 已下载描述文件 → 安装**。
3. **系统设置 → 通用 → 关于本机 → 证书信任设置 → 开启对应 Shadowrocket 证书信任**。

> “配置文件”是指（**配置 → 本地文件**）中正在使用的带 ✔️ 标记的配置。
>
> 多设备同步时，如果配置文件已经包含证书密钥内容，建议直接安装现有证书，而不要重新生成新的 CA 证书。

### 2.4 添加/更新节点订阅失败时

可尝试以下方法：

1. 首页选择一个可用节点，**首页 → 全局路由 → 代理**，再添加/更新节点订阅。
2. 切换网络连接（如关闭 VPN、蜂窝数据改 Wi-Fi、Wi-Fi 改蜂窝数据），再添加/更新节点订阅。
3. 检查节点订阅是否错误或失效，重新获取正确有效的订阅地址。

---

## 三、数据

主要是在日志里查看代理日志（每次开关小火箭就会生成一个日志文件）进行数据分析，具体使用视个人情况而定。

**查看方式：**

- **数据 → 全部 / 代理 / 直连 / 拒绝**，可按分类筛选。
- 每条记录会显示命中的规则、策略组、协议与时间。
- 常用于排查 DNS 泄漏、分流是否命中、某个域名走了代理还是直连。

---

## 四、设置

只设置 **GeoLite2 数据库**，其他保持默认即可。

1. 下滑在 **更新** 里找到 **GeoLite2 数据库**，点击进入。

| 类型 | URL |
| --- | --- |
| 国家 | `https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/Country.mmdb` |
| ASN | `https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/GeoLite2-ASN.mmdb` |

2. 复制粘贴后点击更新即可。

> 其他参数根据自身情况设置。

---

## 五、General 关键参数说明

以下参数通常已包含在配置文件中，如需手动调整，可参考本节说明。

### 5.1 skip-proxy（跳过代理）

此选项强制这些域名或 IP 的连接范围由 Shadowrocket TUN 接口来处理，而不是 Shadowrocket 代理服务器。此选项用于解决一些应用程序的兼容性问题。

`skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com,www.163.com`

### 5.2 tun-excluded-routes（TUN 旁路路由）

Shadowrocket TUN 接口只能处理 TCP 协议。使用此选项可以绕过指定的 IP 范围，让其他协议通过。

`tun-excluded-routes = 10.0.0.0/8, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32, ff02::fb/128`

### 5.3 dns-server（DNS 覆写）

使用普通 DNS 或加密 DNS（如 DoH、DoQ、DoT 等）覆盖默认的系统 DNS。填 `system` 表示使用系统 DNS。

**普通 DNS 示例：**

`dns-server = 223.5.5.5,119.29.29.29`

**加密 DNS 示例：**

- DoH：`dns-server = https://dns.alidns.com/dns-query`
- DoH3：`dns-server = h3://dns.alidns.com/dns-query`
- DoQ：`dns-server = quic://223.5.5.5`
- DoT：`dns-server = tls://223.5.5.5`

**通过代理转发 DNS 查询请求（dns over proxy）示例：**

- `dns-server = https://dns.google/dns-query#proxy=server1`
- `dns-server = https://dns.google/dns-query#ecs=120.76.0.0/14|2620:149:af0::10/56&ecs-override=true`
- `dns-server = https://dns.google/dns-query#proxy=name&ecs=1.1.0.0/14|2620:149:af0::10/56&ecs-override=true`

> **提示：** 如果你在配置模式下出现 DNS 泄漏，优先检查 `dns-server` 是否使用了 `#proxy=节点名`，并确保节点名与 `[Proxy]` 段中定义的完全一致。同时建议关闭 `dns-fallback-system`，避免回退到系统 DNS。

---

## 六、常见问题

### 6.1 为什么全局代理模式不泄漏 DNS，配置模式却泄漏？

- **全局代理模式（Proxy）**：所有流量强制走代理节点，包括 DNS 查询，DNS 在代理服务器端完成，本地不发起请求。
- **配置模式（Config）**：流量按规则分流，但 DNS 查询的走向由 `dns-server` 等参数单独控制，不受“全局走代理”影响。如果 `dns-server` 指向国内 DNS，或 `#proxy=PROXY` 写法未生效，DNS 就会走本地网络，造成泄漏。

**解决思路：**

- `dns-server = https://cloudflare-dns.com/dns-query#proxy=香港 16`
- `fallback-dns-server = https://dns.google/dns-query#proxy=香港 16`
- `dns-direct-system = false`
- `dns-fallback-system = false`

并配合 `hijack-dns` 劫持明文 DNS 请求。

### 6.2 AnyTLS 协议在 Connect 测速下超时，TCP 测速正常？

- **TCP 测速正常**：说明节点本身是活的，域名解析也没问题。
- **Connect 测速超时**：Connect 模式会完整模拟一次代理连接，AnyTLS 对握手超时或会话建立逻辑更敏感，容易在 Connect 模式下超时。

**建议：**

- 以 **TCP 测速** 结果为准判断节点可用性。
- 确保 Shadowrocket 版本在 **2.2.65** 或更高，旧版本对 AnyTLS 支持不完善。
- 如果你不希望测速时解析节点域名，可把所有 `url-test` 组改为 `select` 手动选择。

### 6.3 添加/更新订阅失败？

参考 **2.4 添加/更新节点订阅失败时** 的三种方法。

---

## 七、推荐阅读顺序

1. **首页**：添加节点 → 设置全局路由为“配置”。
2. **配置**：下载配置文件 → 使用配置 → 安装 HTTPS 解密证书。
3. **设置**：更新 GeoLite2 数据库。
4. **数据**：查看日志，确认分流与 DNS 是否符合预期。
5. **常见问题**：遇到 DNS 泄漏或测速异常时查阅。

<!-- SHADOWROCKET_END -->

</details>

<details>
<summary><b>📄 点击展开 / 折叠查看：Surge 设置指南</b></summary>

<br>

<!-- SURGE_START -->

# Surge 使用设置

> 本文档面向 iOS / iPadOS / macOS 上的 Surge，涵盖设置向导、从 URL 安装配置、Host 修改、Proxy Group 修改与使用说明。
> 首次使用建议按“设置向导 → 从 URL 安装配置 → Host 修改 → Proxy Group 修改 → 使用说明”的顺序阅读。

---

## 一、设置向导

### 1.1 配置当前设备

- 设置为系统代理 ✅
- 启动增强模式 ✅

> [!WARNING]
> 不开启增强模式会导致默认使用原生的 TCP/UDP 协议通信的软件或网站无法使用。

- 在 Surge 启动时显示该向导 ✅

- 点击继续。

---

## 二、从 URL 安装配置

### 2.1 入口位置

左侧菜单栏最下面 → **更多** → **配置** → **从 URL 安装配置**。

### 2.2 配置文件地址

    https://raw.githubusercontent.com/VoGter0616/VoGter_Clash/main/cfg/Surge_basic.conf

> [!TIP]
> 复制粘贴后点击下载，等待下载完成即可。Raw 地址需要代理才可以正常访问 GitHub 下载。如果没有代理条件，可以把上述地址转换成国内 CDN 地址，再复制粘贴并下载即可使用。
>
> 提示词：`转换成 testingcf.jsdelivr.net/加速连接`

> [!TIP]
> 下载完成后，右键 `Surge_basic` 选择 **在文本编辑器中编辑**。
>
> 根据机场节点协议修改 `Host`，详见 `[Host]` 组标注。
>
> 注意使用的时候一定要将 Surge 的订阅链接填写至“我的节点”，详见 `[Proxy Group]` 组第 7 条。

### 2.3 切换配置

- 修改完成后保存该文件（即覆盖当前文件）。
- 右键顶部菜单栏 Surge 图标 → **切换配置** → 选择 `Surge_basic`。
- 第一次使用会弹出 **外部资源**，选择 **全部更新**。后续可手动更新规则（右键顶部菜单栏 Surge 图标 → **切换配置** → **更新全部外部资源**）。
- **重载配置** 后完成配置。

---

## 三、Host 修改教程

> [!TIP]
> 如无专属 DNS，则忽视此设置。

### 3.1 模板

    [Host]
    # > AnyTLS 节点专用 DNS（按需取消注释，并替换域名与 DNS IP）
    # > 用途：机场 AnyTLS 节点必须使用专用 DNS 解析域名，否则测速超时
    # > 将 your-domain.com 替换为节点实际域名，DoH 替换为机场要求的专用 DNS，可通过逗号符号分隔多个DNS使用
    # *.your-domain.com = server:DoH1,DoH2

### 3.2 AnyTLS 节点专用 DNS 获取方式

1. 直接拉取订阅机场的 Surge 订阅链接内的 Host 数据。
2. 将机场 / Surge 订阅链接复制到浏览器，自动下载生成 `.conf` 文件。
3. 使用文本编辑器打开该文件（注意不要双击打开，右键选择打开方式）。
4. 在 `[Host]` 里找到该机场节点的域名以及后方的 DNS。
5. 按照通配符的书写方式，把机场 AnyTLS 协议节点的域名和 DNS 按照上述格式进行复制粘贴并修改。

> 注意每个域名搭配一个 DNS。

### 3.3 示例

    [Host]
    # > AnyTLS 节点专用 DNS（按需取消注释，并替换域名与 DNS IP）
    # > 用途：机场 AnyTLS 节点必须使用专用 DNS 解析域名，否则测速超时
    # > 将 your-domain.com 替换为节点实际域名，DoH 替换为机场要求的专用 DNS，可通过逗号符号分隔多个DNS使用
    *.abc.com = server:https://abc.xxx.com/dns1_query,https://abc.xxx.com/dns2_query

---

## 四、Proxy Group 修改教程

> [!WARNING]
> 注意一定要用你所使用机场的 Surge 订阅链接覆盖 `policy-path=` 里的内容，否则没有节点。
>
> `policy-regex-filter` 用来剔除不需要的节点，按需求修改正则表达式内的内容可以剔除不需要的节点。

### 4.1 模板

    # --- 7. 节点引入入口 ---
    # > policy-regex-filter 用来剔除不需要的节点，按需求修改正则表达式内的内容
    # > 注意：请把 https://你的机场订阅链接 替换为真实的 Surge 格式订阅链接
    我的节点 = smart, policy-path=https://你的机场订阅链接, policy-regex-filter=^((?!(流量|官网|过期|剩余)).)*$, update-interval=86400, no-alert=true, hidden=false, include-all-proxies=true

### 4.2 参数说明

| 参数 | 说明 |
| --- | --- |
| `smart` | 使用 Surge 的 smart 策略组 |
| `policy-path` | 机场 Surge 格式订阅链接，必须替换为真实地址 |
| `policy-regex-filter` | 节点名过滤正则，用于剔除“流量 / 官网 / 过期 / 剩余”等无用节点 |
| `update-interval=86400` | 每 24 小时更新一次订阅 |
| `no-alert=true` | 更新时不弹窗提示 |
| `hidden=false` | 在策略组列表中显示该组 |
| `include-all-proxies=true` | 包含订阅中全部节点 |

---

## 五、使用说明

- 右键顶部菜单栏 Surge 图标 → **出站模式** → 选择 **规则判定**。
- 第一次使用，在 **我的节点** 里选择 **重新测速**。
- 下方的规则默认使用最优节点，也可根据自己需求点击修改。

> [!WARNING]
> 该设置已满足当前主机代理分流上网，还需要其他增值设置的自行去 YouTube 学习设置。
>
> 教程中使用的配置是 VoGter 个人使用，该配置文件开源于 GitHub，出现任何问题均与 VoGter 无关。如有需要增加规则，可自行在 Surge 配置里进行修改。
>
> 规则集数据来源于 blackmatrix7 大佬，由衷感谢大佬无私奉献。

---

## 六、推荐阅读顺序

1. **设置向导**：配置当前设备 → 开启系统代理与增强模式。
2. **从 URL 安装配置**：下载 `Surge_basic.conf` → 编辑 Host 与 Proxy Group → 切换配置 → 更新外部资源 → 重载配置。
3. **Host 修改**：按需配置 AnyTLS 节点专用 DNS。
4. **Proxy Group 修改**：替换 `policy-path` 为真实订阅链接，按需调整 `policy-regex-filter`。
5. **使用说明**：出站模式设为“规则判定”，在我的节点里重新测速。

<!-- SURGE_END -->

</details>

---

## 🙏 致谢

> [!IMPORTANT]
> 仅根据自己使用情况进行更新。
>
> 大部分规则来源于以下项目，感谢各位大佬的代码开源。如有侵权，告知即删。

| 项目 | 地址 |
| :--- | :--- |
| Aethersailor / Custom_OpenClash_Rules | https://github.com/Aethersailor/Custom_OpenClash_Rules/tree/main/rule |
| blackmatrix7 / ios_rule_script | https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Clash |
| v2fly / domain-list-community | https://github.com/v2fly/domain-list-community/tree/master/data |
| MetaCubeX / meta-rules-dat | https://github.com/MetaCubeX/meta-rules-dat/tree/master |
| ACL4SSR / ACL4SSR | https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash/config |
| JohnnySun / geoip | https://github.com/JohnnySun/geoip |

---

## ⚠️ 免责声明

本项目所有配置模板均**开源**在本仓库中，任何人都可以**自由查看、审阅与监督**。

- 所有模板**不含任何后门**，也不包含任何恶意代码或隐蔽逻辑。
- 所有模板仅供**学习、研究与技术交流**使用，请自行评估其合法性、安全性与适用性。
- 使用本项目内容所产生的**一切风险与后果，由使用者自行承担**。
- 作者及贡献者**不对任何直接或间接损失负责**，也**无义务**提供技术支持或答疑。
- 如需使用，请自行斟酌后再用。有任何问题，VoGter 均无义务解决。
