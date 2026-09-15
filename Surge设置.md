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

1. 按照通配符的书写方式，把机场 AnyTLS 协议节点的域名和 DNS 按照上述格式进行复制粘贴并修改。

### 3.2 示例

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
