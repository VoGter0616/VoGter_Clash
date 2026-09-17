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

> 全局代理模式（Proxy）下 DNS 通常不走代理，只有配置（Config）模式下才可能正确走代理。如果你更在意 DNS 防泄漏，建议使用配置模式，并正确设置 `dns-server` 和 `proxy-dns-serve` 参数。

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
