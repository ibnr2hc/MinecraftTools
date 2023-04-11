from discordwebhook import Discord as DiscordWebhook
import requests

DISCORD_WEBHOOK = ""


class Discord:
    def __init__(self, webhook):
        self.client = DiscordWebhook(url=webhook)

    def post(self, content):
        """ Discordにメッセージを送信する

        Args:
            content(string): Discordに送信するメッセージ
        """
        self.client.post(content=content)


def main():
    """DiscordにMinecraftサーバーのIPアドレスを送信する"""
    discord = Discord(DISCORD_WEBHOOK)
    ip = get_ec2_public_ip()
    discord.post(f"[SYSTEM] MinecraftServerを起動しました🥳\nIP: `{ip}`")


def get_ec2_public_ip():
    """EC2のパブリックIPアドレスを返します。

    Returns:
        string: EC2のパブリックIPアドレス
    """
    res = requests.get("https://ifconfig.me")
    return res.text


if __name__ == "__main__":
    main()
