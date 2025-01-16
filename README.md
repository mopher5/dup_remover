# dup_remover.pyの使い方

`dup_remover.py`は、指定されたディレクトリ内の重複画像を検出し、削除するためのPythonスクリプトです。

## 前提条件

このスクリプトを実行するには、以下が必要です：
- Python 3.x

## 使い方

1. スクリプトをダウンロードまたはクローンします：

```sh
git clone https://github.com/mopher5/dup_remover.git
cd dup_img
```

2. スクリプトを実行します：

```sh
python dup_remover.py /path/to/your/images
```

`/path/to/your/images`を重複画像を検出したいディレクトリのパスに置き換えてください。

## オプション

- `-d` または `--delete` オプションを使用すると、重複画像を自動的に削除します：

```sh
python dup_remover.py /path/to/your/images --delete
```

## 注意事項

- 重複画像の検出は、画像のハッシュ値を比較することで行います。
- 削除操作は元に戻せないため、実行前に必ずバックアップを取ってください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルを参照してください。

## 貢献

バグ報告や機能提案は、GitHubのIssueトラッカーを使用してください。プルリクエストも歓迎します。
