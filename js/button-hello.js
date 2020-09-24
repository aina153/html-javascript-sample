
// これがjavascriptファイル
// ボタンをクリックすると alert が出る。
document.getElementsByClassName("hello")[0].addEventListener("click",
(e) => {
    alert("ボタンがクリックされました！ ")
})

// 最下部までスクロール
// https://stackoverflow.com/questions/11715646/scroll-automatically-to-the-bottom-of-the-page
document.getElementsByClassName("scroll")[0].addEventListener("click", () => window.scrollTo(0,document.body.scrollHeight))

