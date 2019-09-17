print("グラムをポンドに変換します")
while True:
    gram = input("グラム数を設定してください \n q入力で終了 \n gram = ")
    if (gram == "q"):
        print("変換処理を終了します")
        break
    pound = float(gram) / 453.592
    print("{} グラムは、 {} ポンドです".format(gram, pound))
