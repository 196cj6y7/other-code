# 宣告 Word 物件
$word = New-Object -ComObject Word.Application

# 設定是否顯示 Word 視窗
$word.Visible = $False

# 開啟指定路徑的 Word 文件
$document = $word.Documents.Open("F:\out\word\測試文件.doc")

# 取得表格中第二行第4欄的內容
$table = $document.Tables.Item(1)
$cell = $table.Cell(2, 4)
$text = $cell.Range.Text

# 尋找特定字串的位置
$search_text = "鍋爐組"
$range = $cell.Range
$found = $range.Find.Execute($search_text)#要搜尋的字串

$linkRange = $range.Duplicate()
$linkTarget = 'https://www.google.com/' # 要連結到的檔案路徑
$hyperlink = $document.Hyperlinks.Add($linkRange, $linkTarget)
# 關閉 Word 文件
$document.Close()

# 關閉 Word
$word.Quit()

# 釋放資源
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
