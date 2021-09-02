# linebot-with-python_heroku

特にクリエイティブことはしていません。pythonでLinebotを作り、herokuで運用するまでをまとめています。
サンプルのapp.pyはオウム返しをするだけのbotなので適宜中身を変えてください。
（つまりREADMEがメイン）

Herokuでサンプルボットを作成するLINE公式ドキュメント
https://developers.line.biz/ja/docs/messaging-api/building-sample-bot-with-heroku/

LINE-BOT-SDK for python
https://github.com/line/line-bot-sdk-python

まずLINEDevelopersに登録してください（気が向いたらまとめるかも）
https://developers.line.biz/ja/
新規プロバイダーでappを作成

開発環境はVScodeで行いました。

手順１（LINEBOTを作る）
=====

好きなディレクトリに移動してください。
まず作業する仮想環境を作り、アクティブにしてください。アクティブの仕方はmacとwindowsで変わります。
今回はlineという名前で作りました、適宜変更してください。(line)と始めに出ればOK

    $ python3 -m venv line

windows(コマンドプロンプト)
--------

    $ line\Scripts\active.bat

windows(PowerShell)
--------

    $ line\Scripts\Activate.ps1

mac
--------

    $ line/bin/activate
    

次にflask,line-bot-sdkをインストール

    $ pip install flask
    $ pip install line-bot-sdk
    

同じディレクトリにapp.pyを作ります。（レポジトリ内のはほとんどサンプル通り）

flaskを起動させることでURLが出力されるのでそこにOKと出ていればよし。（Warningが出るようですが大丈夫です。）


    $ flask run

次にLINEアカウントとリンクさせます。

LineDeveloperのページで

「Messaging API 設定」にチャネルアクセストークン

「チャネル基本設定」にチャネルシークレット

があるのでそれぞれ発行し、app.pyの

    line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN') //YOUR_CHANNEL_ACCESS_TOKEN = チャネルアクセストークン
    
    handler = WebhookHandler('YOUR_CHANNEL_SECRET') //YOUR_CHANNEL_SECRET = チャネルシークレット

にそれぞれ入力しましょう。

ローカルでのテスト用のWebページを作るのにngrokを使います。(https://ngrok.com/)
好きな場所に保存、解凍した後、flask runするターミナルとは別のターミナルで保存場所に移動。
windowsならngrok.exe、Macならngrokが有ると思うので以下のコマンドを実行して動かします。

    $ ngrok.exe http 5000 //Windows

または

    $ ./ngrok http 5000 // Mac

また、flask runするとngrokを動かしているターミナルで

Forwardingに

     //https://xxxxxxxxxxx.ngrok.io -> http://localhost:5000 (xxxxxxxxxxxが任意に決まると思います)
    
が有ると思うので

https://xxxxxxxxxxx.ngrok.io にアクセスするとflaskを起動させた時にでたURLと同じようにOKが出ると思います。

これで一時的にですが全世界に公開されているので、このURLをLineDeveloperのページで「Messaging API 設定」のWebhookURLに設定することでLINEbotにアクセスできる様になります。

（※注意　Webhookとして設定するときはURLの最後に/callbackをつけた https://xxxxxxxxxxx.ngrok.io/callback を設定してください）

このあと、LineDeveloperのページで「Messaging API 設定」にあるLINE公式アカウント機能の設定から
Webhookを有効化すると作ったプログラムでLINEbotが動くようになります。

ここで開発を進めましょう。


手順２（Herokuにアップロードする）
=====
完成したら公開しましょう。

まず、herokuに登録してください。
サインイン後、自分のページで右上に[New]といのが有ります。ここでCreate new appとしてください。
AppNameを設定してクリエイトしてください。

HerokuCLIを使ってHeroku上に作ったプログラムをアップしてきます。
Deployを読むとInstall Heroku CLIを見つけることが出来るのでここからDownloadしてください。

windowsならインストーラーをダウンロードし起動

MacOSなら

     brew tap heroku/brew && brew install heroku
     
でインストール出来ます。

次にHerokuにpushする前にrequirement.txtとProfileを作ります。（herokuサーバ上の環境を整えるため）
requirements.txtを手作業で作ると大変なのでgunicornを近います。

     $ pip install gunicorn
     
でインストールし、

     $ pip install > requrirements.txt
     
をするとrequirements.txtが作れます。
（今までインストールしてきたライブラリが記述されています。）

ProcfileはHeroku上でプログラムを動かすのに必要です。

後はHerokuのDeployにある通り進めます。

     $ heroku login
     $ heroku git:clone -a (app名)
     $ git add .
     $ git commit -am "make it better"
     $ git push heroku master

この最後にhttps://（app名）.herokuapp.com/ にデプロイ出来たという出力がされるので、

https://（app名）.herokuapp.com/ にアクセスし、今までと同様OKが出たらOKです。

最後にこのURLに/callbackを加えたhttps://（app名）.herokuapp.com//callback をwebhookに設定して動作確認を終えたら終了です。

お疲れ様でした。
