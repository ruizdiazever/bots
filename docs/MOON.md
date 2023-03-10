# Moon đ

This bot sends a message via Telegram when the price of BTC, ETH, ADA or others is at a maximum or minimum set by you.
![alt](img.png)

## Requirements đ

* Your [Telegram bot](https://core.telegram.org/bots)
* Your Coinbase API credentials
* Python >= 3.11

## Want to try it? đ

1. Create a `.env` file with your phone number and your Coinbase and Telegram credentials.

    ```bash
    COINBASE_API_KEY=''
    COINBASE_API_SECRET=''
    TELEGRAM_TOKEN=''
    TELEGRAM_CHAT_ID=''
    ```

2. Set your preferences in `config.json`, example to use only Telegram bot
3. Run (only in GNU/Linux or MacBook)

    ```bash
    sh moon.sh                # Other Linux system đ§
    sh raspberry_moon.sh          # Raspberry Pi OS đ
    ```

## Useful commands đ§

```bash
ps aux | grep python               # See active process
cd /proc/$pid/fd && tail -f *      # See proc with PID
du -sh logs.log                    # See size of file
docker logs -f $cointainerID       # See live logs
bashtop                            # See system monitor
docker exec -it $containerId bash  # Bash in container
```

## Info âšī¸

* [Installation of Docker in Raspberry OS](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script)
* [Telegram docs about bot messages](https://core.telegram.org/bots/api#message)
* [Coinbase API docs](https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-users)

[MIT License](./LICENSE.md)