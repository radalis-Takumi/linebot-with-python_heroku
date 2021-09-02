# linebot-with-python_heroku

特にクリエイティブことはしていません。pythonでLinebotを作り、herokuで運用するまでをまとめています。
（つまりREADMEがメイン）

Herokuでサンプルボットを作成するLINE公式ドキュメント
https://developers.line.biz/ja/docs/messaging-api/building-sample-bot-with-heroku/

LINE-BOT-SDK for python
https://github.com/line/line-bot-sdk-python

まずLINEDevelopersに登録してください（気が向いたらまとめるかも）
https://developers.line.biz/ja/
新規プロバイダーでappを作成

開発環境はVScodeで行いました。

手順
=====

好きなディレクトリに移動してください。
まず作業する仮想環境を作り、アクティブにしてください。アクティブの仕方はmacとwindowsで変わります。
今回はlineという名前で作りました、適宜変更してください。(line)と始めに出ればOK
::

    $ python3 -m venv line

windows(コマンドプロンプト)
--------
::

    $ line\Scripts\active.bat

windows(PowerShell)
--------
::

    $ line\Scripts\Activate.ps1

mac
--------
::

    $ line/bin/activate
    

次にflask,line-bot-sdkをインストール
::

    $ pip install flask
    $ pip install line-bot-sdk
    

同じディレクトリにapp.pyを作ります。（レポジトリ内のはほとんどサンプル通り）
flaskを起動させることでURLが出力されるのでそこにOKと出ていればよし。（Warningが出るようですが大丈夫です。）

::

    $ pip install flask


