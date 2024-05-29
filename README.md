# StreamlitCamera
カメラ撮影と画像表示アプリ

## 目次
- [プロジェクト概要](#プロジェクト概要)
- [特徴](#特徴)
- [技術スタック](#技術スタック)
- [アプリの使用方法](#アプリの使用方法)
  - [Streamlit Cloudを使用する](#streamlit-cloudを使用する)
  - [Google Colabを使用する](#google-colabを使用する)
- [注意](#注意)
- [コントリビューション](#コントリビューション)

## プロジェクト概要
このプロジェクトは、カメラを使用して画像を撮影し、表示するシンプルなStreamlitアプリです。Streamlit Cloudを利用してデプロイされています。

## 特徴
- カメラを使用してリアルタイムで画像を撮影
- アップロードした画像や撮影した画像を表示
- 直感的なウェブインターフェース

## 技術スタック
- Streamlit
- OpenCV
- Pillow

## アプリの使用方法
### Streamlit Cloudを使用する
Streamlit Cloudでホストされているため、特別な実行手順は不要です。以下のURLからアクセスできます：
[Streamlit Cloud Demo](https://appcamera-49bjbgvn9uxypnzedgruc6.streamlit.app/)

### Google Colabを使用する
Google Colabでアプリを実行する方法については、以下の手順に従ってください：

アプリの起動：
    ```python
    # ngrokを介してStreamlitを公開
    public_url = ngrok.connect(addr='8501')
    print('Public URL:', public_url)
    ```

    公開URLが表示されたら、表示されたURLをクリックしてアプリケーションにアクセスします。

## 注意
このアプリはデモ用途に最適化されています。実際のアプリケーションで使用する場合は、セキュリティやプライバシーに関する考慮が必要です。

## コントリビューション
プロジェクトへのコントリビューションに興味がある方は、Pull RequestやIssueを通じてご提案ください。

## バージョンアップ情報
- **Version 1.0**: 基本機能としてカメラでの画像撮影と表示を提供。
