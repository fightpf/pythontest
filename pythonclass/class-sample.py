class temptest:
    sample=3
    def test(temp_str):
        print("此為物件中的test函式的變數內容:",temp_str)

print(temptest().sample)
temptest.test("測試")