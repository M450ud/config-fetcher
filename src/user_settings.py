# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
            "https://raw.githubusercontent.com/4n0nymou3/wg-config-fetcher/refs/heads/main/configs/wireguard_configs.txt",
            "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
            "https://raw.githubusercontent.com/valid7996/Gozargah/refs/heads/main/Gozargah_Sub",
            "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/refs/heads/main/custom/ipv6.txt",
            "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/refs/heads/main/custom/mahsa.txt",
            "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/refs/heads/main/custom/udp.txt",
            "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/hysteria",
            "https://t.me/s/FreeV2rays/",
            "https://t.me/s/v2ray_free_conf/",
            "https://t.me/s/PrivateVPNs/",
            "https://t.me/s/IP_CF_Config/",
            "https://t.me/s/shadowproxy66/",
            "https://t.me/s/OutlineReleasedKey/",
            "https://t.me/s/prrofile_purple/",
            "https://t.me/s/proxy_shadosocks/",
            "https://t.me/s/meli_proxyy/",
            "https://t.me/s/DirectVPN/",
            "https://t.me/s/VmessProtocol/",
            "https://t.me/s/oneclickvpnkeys/",
            "https://t.me/s/V2ray_Raha/",
            "https://t.me/s/VPN_Accounti/",
            "https://t.me/s/V2rayNG3/",
            "https://t.me/s/V2ray_Alpha/",
            "https://t.me/s/meli_proxyy/",
            "https://t.me/s/VlessConfig/",
            "https://t.me/s/RadixVPN/",
            "https://t.me/s/ELiV2RAY/",
            "https://t.me/s/flyv2ray/",
            "https://t.me/s/V2RayTz/",
            "https://t.me/s/Maznet/",
            "https://t.me/s/DailyV2RY/",
            "https://t.me/s/ShadowsocksM/",
            "https://t.me/s/ViProxys/",
            "https://t.me/s/heyatserver/",
            "https://t.me/s/vpnfail_vless/",
            "https://t.me/s/vlessh",
            "https://t.me/s/v2rayngvpn"
        ]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 500

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 30
