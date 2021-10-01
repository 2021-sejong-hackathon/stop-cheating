const express = require('express');
const router = express.Router();

// 라우터 파일 가져오기
router.get('/hi', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

router.get('/demo', (req, res) => {
    res.sendFile(__dirname + '/demo.html');
})

router.get('/ejs', (req, res) => {
    res.render('hello');
})
// 라우터 파일 등록하기



module.exports = router;