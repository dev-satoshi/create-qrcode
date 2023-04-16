import qrcode

# QRコードを生成
img = qrcode.make("https://www.apple.com/jp/")
# ファイルに保存
img.save("qrcode.png")