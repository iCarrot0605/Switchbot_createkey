# Switchbot_createkey
Switchbot API V1.1を利用して、Keypadにパスコードを追加するデモです。

tokenとsecretはSwitchbot App（V6.14以降）で、「プロフィール」＞「設定」へと進み、「アプリバージョン」のフィールドを10回タップすると表示される「開発者向けオプション」から取得することができます。**これらは他人に公開しないようにしてください。**

## 問題点

```
{'statusCode': 100, 'body': {'commandId': 'CMD166636073309219'}, 'message': 'success'}
```
statusCodeからは、問題なくパスコードが登録できたように見えるのですが、Switchbot Appなどからは登録したコードが見えません。現在、その理由を解明中です。
